#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    content = f.read()
    print("---\n")
    print(f"{content}\n")
    print("---")
    f.close()
    print(f"File '{filename}' closed.")

    lines = content.splitlines()
    new_lines = [line + '#' for line in lines]
    new_content = "\n".join(new_lines)
    print()
    print("Transform data:")
    print("---\n")
    print(new_content)
    print()
    print("---")

    new_file = input("Enter new file name (or empty):")
    if not new_file:
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file}'")
    ftwo = open(new_file, "w")
    ftwo.write(new_content)
    ftwo.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()
