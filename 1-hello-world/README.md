# Ejemplo: Hello World en GitHub Actions

Ejemplo minimo para practicar **GitHub Actions**: cada `push`, `pull request` o ejecucion manual corre un workflow que imprime `Hello World`.

## Contenido

- `.github/workflows/ci.yml`: workflow de Hello World.

## Que hace el workflow

- Se ejecuta en `ubuntu-latest`.
- Imprime un mensaje de Hello World.
- Muestra datos utiles del contexto de GitHub (`repository` y `actor`).

## Como ejecutarlo

1. Sube esta carpeta a un repositorio en GitHub.
2. Haz `git add . && git commit -m "Configura hello world en GitHub Actions" && git push`.
3. Ve a la pestana **Actions** y abre el workflow **Hello World Action**.
4. Revisa el paso **Mostrar mensaje Hello World** para ver el resultado.

## Ejecucion manual (opcional)

1. En la pestana **Actions**, abre el workflow **Hello World Action**.
2. Haz clic en **Run workflow**.
3. Selecciona la rama y confirma con **Run workflow**.
