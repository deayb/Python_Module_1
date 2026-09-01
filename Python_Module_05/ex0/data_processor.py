#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in processor")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):
    def _is_valid_log(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        return all(isinstance(k, str) and
                   isinstance(v, str) for k, v in item.items())

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_valid_log(item) for item in data)
        return self._is_valid_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            converted = f"{item['log_level']}: {item['log_message']}"
            self._storage.append((self._rank, converted))
            self._rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    numeric.ingest(data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")
    print()
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    data_text = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data_text}")
    text.ingest(data_text)
    print("Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f"Text value {rank}: {value}")
    print()

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logg = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing Data: {logg}")
    log.ingest(logg)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
