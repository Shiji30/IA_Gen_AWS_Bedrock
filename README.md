# Herramienta de Marketing con IA Generativa (Amazon Bedrock)

Este proyecto es una aplicación web interactiva desarrollada en Python con Streamlit que utiliza los modelos fundacionales de Amazon Bedrock para potenciar tareas de marketing creativo.

## 🚀 Características Principales

### 1. 🎨 Generación de Imágenes
Utiliza **Amazon Titan Image Generator G1 v2** para crear imágenes de alta calidad a partir de descripciones de texto.
- Interfaz intuitiva para ingresar prompts.
- Opción de mejora de prompts utilizando IA (Claude).
- Selección de estilos artísticos (Cinemático, Fotográfico, 3D, etc.).
- Descarga directa de las imágenes generadas.

### 2. 📝 Editor de Contenido
Refina y transforma textos utilizando **Anthropic Claude 3 Haiku**.
- Corrección gramatical y ortográfica.
- Resumen de textos largos.
- Cambio de tono (más profesional, creativo, etc.).
- Traducción y expansión de ideas.

### 3. 🖼️ Galería de Activos
- Visualiza todas las imágenes generadas anteriormente.
- Descarga activos desde el historial.
- Persistencia local de imágenes y metadatos.

## 🛠️ Requisitos Previos

- **Python 3.8** o superior.
- Una cuenta de **AWS** activa con permisos para acceder a Amazon Bedrock.
- Acceso habilitado en AWS Bedrock para los siguientes modelos:
  - **Amazon Titan Image Generator G1 v2** (`amazon.titan-image-generator-v2:0`)
  - **Anthropic Claude 3 Haiku** (`anthropic.claude-3-haiku-20240307-v1:0`)

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio** (o descargar los archivos):
   Asegúrate de tener todos los archivos del proyecto en tu máquina local.

2. **Crear un entorno virtual** (Recomendado):
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar Variables de Entorno**:
   Crea un archivo llamado `.env` en la raíz del proyecto (puedes usar `.env.example` como guía) y agrega tus credenciales de AWS:
   ```ini
   AWS_ACCESS_KEY_ID=TU_ACCESS_KEY
   AWS_SECRET_ACCESS_KEY=TU_SECRET_KEY
   AWS_REGION=us-east-1
   ```

## ▶️ Ejecución de la Aplicación

### Opción 1 (PowerShell - Recomendada)
Haz clic derecho en `run_app.ps1` y selecciona "Ejecutar con PowerShell". Esto evita bloqueos de seguridad de Windows comunes con archivos .bat.

### Opción 2 (Terminal)
Desde la terminal, con el entorno virtual activado, ejecuta:
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado (usualmente en http://localhost:8501).

## 📂 Estructura del Proyecto

- `app.py`: Archivo principal y página de inicio.
- `pages/`: Contiene las páginas de la aplicación (Generación, Editor, Galería, Configuración).
- `utils/`:
  - `bedrock.py`: Lógica de conexión con AWS Bedrock.
  - `db.py`: Gestión de base de datos local (SQLite) para historial.
  - `auth.py`: Manejo simple de sesión de usuario.
- `generated_images/`: Directorio donde se guardan las imágenes creadas.
- `app.db`: Base de datos SQLite local.
- `run_app.ps1`: Script de inicio seguro para Windows.

## ⚠️ Nota sobre el Modelo de Texto
El proyecto está configurado para usar **Meta Llama 3 8B Instruct** (`meta.llama3-8b-instruct-v1:0`) para las tareas de texto. Este modelo es rápido, potente y generalmente no requiere aprobaciones de "casos de uso" complejas como otros modelos. Asegúrate de tener habilitado el acceso a **Llama 3 8B Instruct** en la consola de AWS Bedrock (Model Access).
