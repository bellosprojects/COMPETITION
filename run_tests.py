"""
usage: python run_tests.py [--tests-dir DIR][--solutions-dir DIR][--json-out FILE]
"""

import argparse
import glob
import json
import subprocess
import sys
from pathlib import Path

PROBLEMS = {
    1: {"weight": 4, "timeout": 10},
    2: {"weight": 6, "timeout": 10},
    3: {"weight": 5, "timeout": 10},
    4: {"weight": 5, "timeout": 10},
}

def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())

def run_case_cmd(cmd: list[str], input_text: str, timeout: int) -> tuple[str, str | None]:
    try:
        result = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode != 0:
            stderr_last = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "(sin stderr)"
            return result.stdout, f"exit {result.returncode}: {stderr_last}"

        return result.stdout, None
    except subprocess.TimeoutExpired:
        return "", "timeout"
    except Exception as e:
        return "", f"crash: {type(e).__name__}"

def find_solution(solutions_dir: Path, pid: int) -> Path | None:
    for ext in (".py", ".cpp", ".cc", ".cxx"):
        candidate = solutions_dir / f"solucion{pid}{ext}"
        if candidate.exists():
            return candidate

    return None

def prepare_solution(solution: Path) -> tuple[list[str], str | None]:
    suffix = solution.suffix.lower()

    if suffix == ".py":
        return [sys.executable, "-X", "faulthandler", str(solution)], None

    if suffix in (".cpp", ".cc", ".cxx"):
        binary = solution.with_suffix("")
        try:
            cr = subprocess.run(
                ["g++", "-02", "-std=c++17", "-o", str(binary), str(solution)],
                capture_output=True, text=True, timeout=30
            )
        except subprocess.TimeoutExpired:
            return [], "compilacion timeout (>30s)"

        if cr.returncode != 0:
            last = (cr.stderr.strip().splitlines() or ["(sin stderr)"])[-1]
            return [], f"Compilacion fallo: {last}"
        return [str(binary)], None

    return [], f"Extension no soportada: {suffix}"

def evaluate_problem(pid: int, test_dir: Path, solutions_dir: Path) -> dict:
    config = PROBLEMS[pid]
    case_dir = test_dir / f"p{pid}"

    result = {
        "id": pid,
        "weight": config['weight'],
        "passed": 0,
        "failed": 0,
        "total": 0,
        "score": 0.0,
        "errors": [],
    }

    input_files = sorted(glob.glob(str(case_dir / "*.in")))
    result['total'] = len(input_files)

    solution = find_solution(solutions_dir=solutions_dir, pid=pid)
    if solution is None:
        result['failed'] = result['total']
        result['errors'].append(f"Archivo no encontrado: solucion{pid}.(py|cpp)")
        return result

    cmd, prep_error = prepare_solution(solution)

    if prep_error:
        result['failed'] = result['total']
        result['errors'].append(prep_error)
        return result

    for in_path in input_files:
        out_path = Path(in_path).with_suffix(".out")
        if not out_path.exists():
            result['errors'].append(f"{Path(in_path).name}: falta .out")
            result['failed'] += 1
            continue

        expected = normalize(out_path.read_text(encoding="utf-8-sig"))
        actual_raw, error = run_case_cmd(
            cmd, Path(in_path).read_text(encoding="utf-8-sig"), config['timeout']
        )

        if error:
            result['failed'] += 1
            result['errors'].append(f"{Path(in_path).name}: {error}")
        elif normalize(actual_raw) == expected:
            result['passed'] += 1
        else:
            result['failed'] += 1
            result['errors'].append(f"{Path(in_path).name}: salida incorrecta")

    if result['total'] > 0:
        result['score'] = round(
            result['passed'] / result['total'] * config['weight'], 4
        )

    return result

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests-dir", default="tests")
    parser.add_argument("--solutions-dir", default="solutions")
    parser.add_argument("--json-out", default=None)
    args = parser.parse_args()

    tests_dir = Path(args.tests_dir)
    solutions_dir = Path(args.solutions_dir)

    problems = [evaluate_problem(pid, tests_dir, solutions_dir) for pid in sorted(PROBLEMS)]
    total_score = round(sum(p['score'] for p in problems), 4)
    max_score = sum(p['weight'] for p in PROBLEMS.values())

    summary = {
        "problems": problems,
        "total_score": total_score,
        "max_score": max_score
    }

    output = json.dumps(summary, indent=2, ensure_ascii=False)
    if args.json_out:
        Path(args.json_out).write_text(output, encoding="utf-8")
    print(output)

if __name__ == "__main__":
    main()