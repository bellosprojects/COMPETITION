# Competencia de Programación

¡Bienvenido/a! Este repositorio contiene el enunciado y las plantillas para participar en la competencia.

## Requisitos previos

* Tener Python3 instalado 
* Tener una cuenta de GitHub
* Tener Git instalado
* Un editor de codigo (VSCode de preferencia)
* Pylance (extension de vscode) u otro IntelliceSence

## Fechas Importantes
*   **Inicio:** Sin confirmar
*   **Cierre de envíos:** Sin confirmar
*   **Anuncio de resultados:** En el canal `#results` de nuestro Discord.

> **Importante:** Solo se evaluarán las soluciones cuyo **Pull Request esté abierto antes de la fecha y hora de cierre**. Los commits posteriores no se tendrán en cuenta.

## ¿Cómo participar? (Paso a Paso)

### 1. Haz un Fork de este repositorio
En la página principal de este repo, haz clic en el botón **"Fork"** (arriba a la derecha). Esto creará una copia personal del repositorio en tu cuenta de GitHub. Solo necesitas hacerlo **una vez** al principio.

### 2. Clona tu Fork y trabaja localmente
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/TU_USUARIO/competition.git
cd competition
```
Implementa tu solución en los archivos que se indican en `INSTRUCTIONS.md`. Usa las plantillas de la carpeta `soluciones/` como punto de partida; **no cambies los nombres de los archivos**.

### 3. Crea una rama para tu solución
```bash
git checkout -b solucion-tu-usuario
```
Puedes usar el nombre de rama que prefieras, pero que sea descriptivo.

### 4. Haz commit y push a tu Fork
```bash
git add .
git commit -m "Solución de [tu nombre]"
git push origin solucion-tu-usuario
```

### 5. Abre un Pull Request (PR) hacia este repositorio
Ve a la página de tu Fork en GitHub. Verás un botón que dice **"Compare & pull request"**. Haz clic, asegúrate de que la rama base sea `main` de **este** repositorio y la rama de comparación sea la tuya. Rellena el título y la descripción, y crea el PR.

> **Este es el paso más importante.** Sin un PR abierto hacia este repositorio, tu solución no será evaluada.

### 6. ¿Y si necesito corregir algo?
No hace falta que abras otro PR. Simplemente haz nuevos `commit` y `push` a la misma rama (`solucion-tu-usuario`) en tu Fork. El Pull Request que ya abriste se actualizará automáticamente con los nuevos cambios.

## ¿Cómo se evalúa mi solución?
Al abrir o actualizar tu PR, un sistema automático ejecutará una serie de pruebas sobre tu código. **No podrás ver los casos de prueba**, ya que son privados para garantizar una evaluación justa. El resultado (puntuación y casos superados) se publicará en el canal `#results` de Discord.

## Preguntas Frecuentes
*   **¿Puedo usar librerías externas?** No, salvo que se indique lo contrario en `statements.md`. El entorno de evaluación usa la librería estándar.
*   **¿Puedo modificar el archivo `run_tests.py`?** No. El evaluador utiliza una versión propia e inalterable de ese script.
*   **¿Qué pasa si mi PR falla las pruebas?** Puedes seguir haciendo commits para corregir los errores hasta la fecha de cierre.