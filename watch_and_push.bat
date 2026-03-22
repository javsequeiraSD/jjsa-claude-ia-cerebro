@echo off
:: watch_and_push.bat — Auto-sync CLAUDE.IA → GitHub
:: Detecta cambios en la carpeta y hace push automatico
:: Ejecutar con doble clic — corre en background

cd /d "%~dp0"

echo [CLAUDE.IA Watcher] Iniciando sincronizacion automatica...
echo [CLAUDE.IA Watcher] Carpeta: %~dp0
echo [CLAUDE.IA Watcher] Presiona Ctrl+C para detener

:loop
:: Espera 30 segundos
timeout /t 30 /nobreak >nul

:: Verifica si hay cambios
git diff --quiet && git diff --cached --quiet
if errorlevel 1 (
    :: Hay cambios — commit y push
    for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set FECHA=%%c-%%a-%%b
    for /f "tokens=1-2 delims=: " %%a in ("%time%") do set HORA=%%a:%%b
    git add -A
    git commit -m "auto: sync %FECHA% %HORA%"
    git push origin main
    echo [%HORA%] Push realizado
) else (
    :: Sin cambios
    echo [%time:~0,5%] Sin cambios
)

goto loop
