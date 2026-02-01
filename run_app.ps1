Write-Host "Iniciando Generative AI Marketing Tool..." -ForegroundColor Cyan
Write-Host "----------------------------------------" -ForegroundColor Cyan

# Check for venv
$VenvPath = ".\venv\Scripts\Activate.ps1"
if (Test-Path $VenvPath) {
    # Activate venv using dot sourcing
    . $VenvPath
    if ($?) {
        Write-Host "Entorno virtual activado." -ForegroundColor Green
    } else {
        Write-Host "Error al activar entorno virtual." -ForegroundColor Red
        Pause
        Exit
    }
} else {
    Write-Host "Advertencia: No se detectó carpeta venv. Ejecutando con Python del sistema..." -ForegroundColor Yellow
}

# Run Streamlit
streamlit run app.py

Pause
