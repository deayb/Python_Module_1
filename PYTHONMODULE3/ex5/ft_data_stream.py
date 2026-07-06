#!/usr/bin/env python3

import typing
import random

PLAYERS = [
    "bob", "alice", "dylan", "charlie"
]

ACTIONS = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def generate_events() -> None:
    events = gen_event()

    for i in range(1000):
        name, actions = next(events)
        print(f"Event {i}: Player {name} did action {actions}")


def build_list() -> list[tuple[str, str]]:
    event_list = []
    events = gen_event()
    for _ in range(10):
        event = next(events)
        event_list.append(event)
    print(f"Built list of 10 events: {event_list}")
    return event_list


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generate_events()
    my_list = build_list()

    for event in consume_event(my_list):
        print(f"Got event form list: {event}")
        print(f"Remains in list: {my_list}")
