#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
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


if __name__ == "__main__":
    main()
