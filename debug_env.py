import os
from dotenv import load_dotenv

load_dotenv()

ak = os.getenv("AWS_ACCESS_KEY_ID", "NOT_FOUND")
sk = os.getenv("AWS_SECRET_ACCESS_KEY", "NOT_FOUND")

print(f"ACCESS_KEY_ID length: {len(ak)}")
print(f"ACCESS_KEY_ID first 4 chars: {ak[:4]}")
print(f"SECRET_KEY length: {len(sk)}")

if "/" in ak or "+" in ak:
    print("WARNING: Access Key ID contains special characters ('/' or '+'). It usually shouldn't.")
    print("It looks like you might have pasted the Secret Key into the Access Key field!")
