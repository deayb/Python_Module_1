#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    name: str

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @property
    def total_processed(self) -> int:
        return self._rank

    @property
    def remaining(self) -> int:
        return len(self._storage)

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
    name: str = "Numeric Processor"

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
    name: str = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            print(f"{proc.name}: total {proc.total_processed} items processed,"
                  f" remaining {proc.remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_s = DataStream()
    data_s.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    data_s.register_processor(numeric)
    stream: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {stream}")
    data_s.process_stream(stream)
    data_s.print_processors_stats()

    print("\nRegistering other data processors")
    print("Send the same batch again")
    text = TextProcessor()
    data_s.register_processor(text)
    log = LogProcessor()
    data_s.register_processor(log)
    data_s.process_stream(stream)
    data_s.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    numeric.output()
    numeric.output()
    numeric.output()
    text.output()
    text.output()
    log.output()
    data_s.print_processors_stats()


if __name__ == "__main__":
    main()
