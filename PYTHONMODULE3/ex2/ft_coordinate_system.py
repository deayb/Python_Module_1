#! /usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = []
            for part in parts:
                coords.append(float(part.strip()))
            return (coords[0], coords[1], coords[2])
        except ValueError as e:
            print(f"Error on parameter '{part.strip()}': {e}")


def main():
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist1 = round(math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2), 4)
    print(f"Distance to center: {dist1}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist2 = round(math.sqrt((pos2[0]-pos1[0])**2 +
                            (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist2}")


if __name__ == '__main__':
    main()
