import os
import sys
import subprocess
import json

# Ensure UTF-8 encoding for subprocess calls
os.environ['PYTHONIOENCODING'] = 'utf-8'

def save_api_key(provider: str, api: str):
    cmd = ["./api_manager/target/release/api_manager.exe", "-s", api, provider]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        raise RuntimeError(
            f"Fail to run api_manager, provider={provider}, stderr: {stderr}"
        ) from e

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"api_manager return incorrect json format: {result.stdout}")
    if data.get("status") != "success":
        raise RuntimeError(
            f"Fail to set {provider} api_key, output: {result.stdout}"
        )

def save_token(provider: str, token: str):
    cmd = ["./api_manager/target/release/api_manager.exe", "-s", token, provider]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        raise RuntimeError(
            f"Fail to run api_manager, provider={provider}, stderr: {stderr}"
        ) from e

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"api_manager return incorrect json format: {result.stdout}")
    if data.get("status") != "success":
        raise RuntimeError(
            f"Fail to set {provider} api_key, output: {result.stdout}"
        )


def delete_api_key(provider: str):
    cmd = ["./api_manager/target/release/api_manager.exe", "-d", provider]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        raise RuntimeError(
            f"Fail to run api_manager, provider={provider}, stderr: {stderr}"
        ) from e

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"api_manager return incorrect json format: {result.stdout}")
    if data.get("status") != "success":
        raise RuntimeError(
            f"Fail to delete {provider} api_key, output: {result.stdout}"
        )

def delete_token(provider: str):
    cmd = ["./api_manager/target/release/api_manager.exe", "-d", provider]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        raise RuntimeError(
            f"Fail to run api_manager, provider={provider}, stderr: {stderr}"
        ) from e

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"api_manager return incorrect json format: {result.stdout}")
    if data.get("status") != "success":
        raise RuntimeError(
            f"Fail to delete {provider} api_key, output: {result.stdout}"
        )
def main():
    provider = sys.argv[1]
    api = sys.argv[2]
    save_api_key(provider=provider, api=api)

if __name__ == "__main__":
    main()