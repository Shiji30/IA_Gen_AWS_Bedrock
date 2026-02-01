@echo off
echo Iniciando Generative AI Marketing Tool...
echo ----------------------------------------

call .\venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error: No se pudo activar el entorno virtual.
    echo Asegurate de haber instalado las dependencias primero.
    pause
    exit /b
)

echo Entorno virtual activado. Ejecutando aplicacion...
streamlit run app.py

pause
