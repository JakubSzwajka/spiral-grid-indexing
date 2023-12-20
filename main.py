from math import sqrt, ceil
from enum import Enum


class RingBar(Enum):
    TOP = "TOP"
    LEFT = "LEFT"
    LOW = "LOW"
    RIGHT = "RIGHT"


def get_bar_for_index(index, last_index, size):
    if index > last_index - size:
        return RingBar.TOP
    elif index > last_index - (size - 1) - size:
        return RingBar.LEFT
    elif index > last_index - ((size - 1) * 2) - size:
        return RingBar.LOW
    else:
        return RingBar.RIGHT


def get_coords_for_index(index, ring_number, ring_last_index):
    last_ring_index_coords = (ring_number, ring_number)
    size = (ring_number * 2) + 1

    ring_bar = get_bar_for_index(index, ring_last_index, size)

    if ring_bar == RingBar.TOP:
        return (
            last_ring_index_coords[0] - (ring_last_index - index),
            last_ring_index_coords[1],
        )
    elif ring_bar == RingBar.LEFT:
        return (
            last_ring_index_coords[0] - size + 1,
            last_ring_index_coords[1] - ((ring_last_index - size + 1) - index),
        )
    elif ring_bar == RingBar.LOW:
        return (
            (last_ring_index_coords[0] - size + 1)
            + (ring_last_index - index - (2 * (size - 1))),
            last_ring_index_coords[1] - size + 1,
        )
    elif ring_bar == RingBar.RIGHT:
        return (
            last_ring_index_coords[0],
            (last_ring_index_coords[1] - size + 1)
            + (ring_last_index - index - (3 * (size - 1))),
        )


def main():
    for index in range(0, 40):
        # Calculate the ring number and last index directly
        ring_number = ceil((sqrt(1 + 8 * (index / 8)) - 1) / 2)
        ring_last_index = ring_number * (ring_number + 1) * 4

        if index <= ring_last_index:
            coords = get_coords_for_index(index, ring_number, ring_last_index)
            print("Index: ", index, coords)
        else:
            print("Index out of bound for current ring calculation.")


if __name__ == "__main__":
    main()
