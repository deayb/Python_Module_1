#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol
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
            raise ValueError("Improper numeric data")
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


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output: ")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        indexs = [index for index, _ in data]
        print("JSON Output: ")
        print(f'"{indexs}": "{values}"')

def main() -> None:
    