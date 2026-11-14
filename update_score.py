"""Update the public competition scoreboard from one evaluation result."""

import argparse
import base64
from datetime import datetime, timezone
import json
from pathlib import Path
import time
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen


def load_json(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def update_scoreboard(scoreboard: dict, result: dict, login: str, avatar: str,
                      run_id: str, run_number: int) -> tuple[dict, str, bool]:
    participants = scoreboard.get("participants", [])
    events = scoreboard.get("events", [])
    if not isinstance(participants, list) or not isinstance(events, list):
        raise ValueError("score.json debe contener listas de participantes y eventos.")

    previous = next(
        (participant for participant in participants if participant.get("login") == login),
        None,
    )
    previous_ranks = {
        participant["login"]: participant.get("rank")
        for participant in participants
    }
    if previous and run_number < previous.get("run_number", 0):
        return scoreboard, "", True

    solved = sorted(
        problem["id"]
        for problem in result["problems"]
        if problem.get("total", 0) > 0 and problem.get("failed") == 0
    )
    prior_solved = set(previous.get("solved", [])) if previous else set()
    now = datetime.now(timezone.utc).isoformat()
    participant = {
        "login": login,
        "avatar_url": avatar,
        "score": result["total_score"],
        "max_score": result["max_score"],
        "solved": solved,
        "problems": [
            {
                key: problem[key]
                for key in ("id", "passed", "failed", "total", "score", "weight")
                if key in problem
            }
            for problem in result["problems"]
        ],
        "run_id": run_id,
        "run_number": run_number,
        "updated_at": now,
    }

    participants = [p for p in participants if p.get("login") != login]
    participants.append(participant)
    participants.sort(key=lambda p: (-p["score"], p["login"].casefold()))
    for rank, entry in enumerate(participants, start=1):
        entry["rank"] = rank
    new_rank = next(p["rank"] for p in participants if p["login"] == login)

    messages = []
    for problem_id in solved:
        if problem_id not in prior_solved:
            event_id = f"{run_id}:solved:{problem_id}"
            if not any(event.get("id") == event_id for event in events):
                events.append({
                    "id": event_id,
                    "type": "solved",
                    "login": login,
                    "problem": problem_id,
                    "created_at": now,
                })
                messages.append(f"✅ **{login}** ha resuelto **P{problem_id}**.")

    old_rank = previous.get("rank") if previous else None
    if old_rank and new_rank < old_rank:
        passed = [
            p["login"]
            for p in participants
            if p["login"] != login
            and previous_ranks.get(p["login"]) is not None
            and previous_ranks[p["login"]] < old_rank
            and p["rank"] > new_rank
        ]
        event_id = f"{run_id}:rebase:{old_rank}:{new_rank}"
        if not any(event.get("id") == event_id for event in events):
            events.append({
                "id": event_id,
                "type": "rebase",
                "login": login,
                "from_rank": old_rank,
                "to_rank": new_rank,
                "overtaken": passed,
                "created_at": now,
            })
            message = f"🏁 **{login}** avanzó al puesto **{new_rank}**"
            if passed:
                message += f", superando a {', '.join(f'**{login}**' for login in passed)}"
            messages.append(message + ".")

    updated = {
        "updated_at": now,
        "participants": participants,
        "events": events[-100:],
    }
    return updated, "\n".join(messages), False


def request_json(url: str, token: str, method: str = "GET", body: dict | None = None):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = Request(url, data=data, headers=headers, method=method)
    with urlopen(request, timeout=20) as response:
        return json.load(response)


def update_remote_scoreboard(repository: str, branch: str, token: str,
                             result: dict, login: str, avatar: str,
                             run_id: str, run_number: int) -> tuple[dict, str]:
    api_url = f"https://api.github.com/repos/{repository}/contents/score.json"
    url = f"{api_url}?ref={quote(branch, safe='')}"

    for attempt in range(5):
        try:
            current = request_json(url, token)
        except HTTPError as error:
            if error.code == 404:
                current = None
            else:
                raise

        if current:
            content = base64.b64decode(current["content"]).decode("utf-8")
            scoreboard = json.loads(content)
            sha = current["sha"]
        else:
            scoreboard = {"participants": [], "events": []}
            sha = None

        updated, message, stale = update_scoreboard(
            scoreboard, result, login, avatar, run_id, run_number
        )
        if stale:
            return scoreboard, ""

        content = json.dumps(updated, ensure_ascii=False, indent=2) + "\n"
        body = {
            "message": "Actualizar marcador de la competencia",
            "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
            "branch": branch,
        }
        if sha:
            body["sha"] = sha

        try:
            request_json(api_url, token, method="PUT", body=body)
            return updated, message
        except HTTPError as error:
            if error.code not in (409, 422) or attempt == 4:
                raise
            time.sleep(0.5 * (attempt + 1))

    raise RuntimeError("No se pudo actualizar score.json después de varios intentos.")


def write_github_output(path: Path, message: str) -> None:
    with path.open("a", encoding="utf-8") as output:
        output.write(f"notify={'true' if message else 'false'}\n")
        output.write("message<<EOF\n")
        output.write(f"{message}\n")
        output.write("EOF\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--login", required=True)
    parser.add_argument("--avatar", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--run-number", required=True, type=int)
    parser.add_argument("--github-output", required=True, type=Path)
    parser.add_argument("--score", type=Path)
    parser.add_argument("--pages-score", type=Path)
    parser.add_argument("--repository")
    parser.add_argument("--branch")
    parser.add_argument("--token")
    args = parser.parse_args()

    result = load_json(args.result, None)
    if not isinstance(result, dict) or not isinstance(result.get("problems"), list):
        raise ValueError("El resultado de evaluación no tiene el formato esperado.")

    if args.score:
        scoreboard = load_json(args.score, {"participants": [], "events": []})
        updated, message, stale = update_scoreboard(
            scoreboard, result, args.login, args.avatar, args.run_id, args.run_number
        )
        if not stale:
            args.score.write_text(
                json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    else:
        if not all((args.repository, args.branch, args.token)):
            parser.error("Se requiere --score o bien --repository, --branch y --token.")
        updated, message = update_remote_scoreboard(
            args.repository, args.branch, args.token, result,
            args.login, args.avatar, args.run_id, args.run_number,
        )

    if args.pages_score:
        args.pages_score.write_text(
            json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    write_github_output(args.github_output, message)


if __name__ == "__main__":
    main()
