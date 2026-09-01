#!/usr/bin/env python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(filename) as f:
                file_cont = f.read()
            return (True, file_cont)
        except OSError as e:
            return (False, str(e))
    elif action == "write":
        try:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except OSError as e:
            return (False, str(e))
    else:
        return (False, f"Unknown action: '{action}'")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    result1 = secure_archive("/etc/shadow")
    result2 = secure_archive("notexistingfile.txt")
    result3 = secure_archive("ancient_fragment.txt")
    result4 = secure_archive(
        "nouveau_fichier.txt", "write", "Bonjour le monde oui"
        )
    print(f"Using 'secure_archive' to read from a nonexistent file:"
          f"\n{result2}\n")
    print(f"Using 'secure_archive' to read from a inaccessible file:"
          f"\n{result1}\n")
    print(f"Using 'secure_archive' to read from a regular file:"
          f"\n{result3}\n")
    print(f"Using 'secure_archive' to write previous content to a new file:"
          f"\n{result4}")
