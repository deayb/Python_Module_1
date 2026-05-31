#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature -> None():
    print("=== Garden Temperature ===\n")
    temp_str = "25"
    print(f"Input data is '{temp_str}'")
    temperature = input_temperature(temp_str)
    print(f"Temperature is now {temperature}°C\n")
    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


test_temperature()
