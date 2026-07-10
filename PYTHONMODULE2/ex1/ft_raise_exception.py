#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if 0 <= temperature <= 40:
        return temperature
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
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
    temp_str = "100"
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    temp_str = "-50"
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
