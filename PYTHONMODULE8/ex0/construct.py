import sys
import os
import site


def main() -> None:

    is_venv = sys.prefix != sys.base_prefix
    path = os.path.basename(sys.prefix)
    pp = sys.executable

    if is_venv:
        print("\nMATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {pp}")
        print(f"Virtual Environment: {path}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print(f"Package installation path: \n{site.getsitepackages()[0]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {pp}")
        print("Virtual Environment: None detected"
              "\n\nWARNING: You're in the global environment!"
              "\nThe machines can see everything you install."
              "\n\nTo enter the construct, run:"
              "\npython -m virtualenv matrix_env"
              "\nsource matrix_env/bin/activate # On Unix\n"
              r"matrix_env\Scripts\activate  # On Windows"
              "\n\nThen run this program again.")


if __name__ == "__main__":
    main()
