import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError, NoCredentialsError

# Force reload of env vars
load_dotenv(override=True)

print("--- Diagnóstico de Credenciales ---")

# 1. Check Env Vars
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")

if access_key:
    print(f"✅ AWS_ACCESS_KEY_ID encontrado: {access_key[:4]}...{access_key[-4:]}")
else:
    print("❌ AWS_ACCESS_KEY_ID no encontrado en variables de entorno.")

if secret_key:
    print(f"✅ AWS_SECRET_ACCESS_KEY encontrado: {'*' * 5}")
else:
    print("❌ AWS_SECRET_ACCESS_KEY no encontrado.")

print(f"📍 Región configurada: {region}")

# 2. Check Boto3 Session
try:
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    sts = session.client('sts')
    identity = sts.get_caller_identity()
    print(f"✅ Credenciales válidas. Identidad: {identity['Arn']}")
except Exception as e:
    print(f"❌ Error al validar credenciales con STS: {e}")
    exit(1)

# 3. Check Bedrock Access
print("\n--- Probando Acceso a Bedrock ---")
try:
    bedrock = session.client('bedrock')
    response = bedrock.list_foundation_models(byProvider='anthropic')
    models = [m['modelId'] for m in response.get('modelSummaries', [])]
    print(f"✅ Conexión a Bedrock exitosa.")
    print(f"ℹ️ Modelos Anthropic disponibles: {len(models)} encontrados")
except ClientError as e:
    print(f"❌ Error de acceso a Bedrock: {e}")
    print("Posible causa: El usuario IAM no tiene permisos para 'bedrock:ListFoundationModels' o Bedrock no está habilitado en esta región.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
