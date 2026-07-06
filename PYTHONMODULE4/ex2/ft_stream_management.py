#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
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
    try:
        ftwo = open(new_file, "w")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {e}\n")
        print("Data not saved.")
        return

    ftwo.write(new_content)
    ftwo.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()
