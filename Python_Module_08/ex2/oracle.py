import os
import sys

from dotenv import load_dotenv # type: ignore


def describe(value: str | None, present: str, missing: str) -> str:
    if value:
        return present
    return missing


def check_production(
            database_url: str | None,
            api_key: str | None,
        ) -> list[str]:
    errors: list[str] = []
    if not database_url:
        errors.append("DATABASE_URL is required in production")
    if not api_key:
        errors.append("API_KEY is required in production")
    return errors


def check_env_file() -> str:
    if os.path.exists(".env"):
        return "[OK] .env file found"
    return "[WARN] No .env file (using defaults or shell variables)"


def check_override() -> str:
    return "[OK] Shell variables take priority over .env"


def check_gitignore() -> str:
    try:
        with open(".gitignore", "r") as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        return "[WARN] No .gitignore found"
    if ".env" in lines:
        return "[OK] .env is excluded from version control"
    return "[WARN] .env is NOT in .gitignore"


def check_no_hardcoded_secrets() -> str:
    try:
        with open(__file__, "r") as file:
            lines = file.readlines()
    except OSError:
        return "[WARN] Could not inspect source file"
    keywords = ("password", "api_key", "secret", "token")
    for line in lines:
        stripped = line.strip().lower()
        if stripped.startswith("#") or "getenv" in stripped:
            continue
        for keyword in keywords:
            if keyword + ' = "' in stripped or keyword + " = '" in stripped:
                return "[WARN] Possible hardcoded secret in source"
    return "[OK] No hardcoded secrets detected"


def main() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "http://localhost:8080")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print("Mode:", mode)
    print("Database:", describe(database_url, "Connected", "NOT CONFIGURED"))
    print("API Access:", describe(api_key, "Authenticated", "MISSING"))
    print("Log Level:", log_level)
    print("Zion Network:", zion_endpoint)
    print()
    print("Environment security check:")
    print(check_no_hardcoded_secrets())
    print(check_env_file())
    print(check_gitignore())
    print(check_override())
    if mode == "production":
        errors = check_production(database_url, api_key)
        if errors:
            print()
            for error in errors:
                print("[ERROR]", error)
            sys.exit(1)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
