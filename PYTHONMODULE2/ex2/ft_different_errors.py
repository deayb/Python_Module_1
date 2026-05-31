#! /usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existant/file")
    elif operation_number == 3:
        "hello" + 123
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    print("Testing operation 0...")
    try:
        garden_operations(operation_number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    operation_number = 1
    print("Testing operation 1...")
    try:
        garden_operations(operation_number)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    operation_number = 2
    print("Testing operation 2...")
    try:
        garden_operations(operation_number)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    operation_number = 3
    print("Testing operation 3...")
    try:
        garden_operations(operation_number)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    operation_number = 4
    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully\n")
    except Exception as e:
        print(f"Unexpected error: {e}")
    print("All error types tested successfully!")


test_error_types()
