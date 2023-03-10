#!/bin/python3

import math
import os
import random
import re
import sys


def segments_max(arr: list, max_distance=0):
    for i in range(1, len(arr)):
        distance = abs(arr[i] - arr[i -1]) # distance
        midpoint = distance // 2
        max_distance = max(max_distance, midpoint)
        print(midpoint)

    return int(max_distance)


def flatlandSpaceStations(n, c):
    length = n
    stations = sorted(c)
    start = stations[0]
    end = stations[-1]

    start_distance = abs(start - 0)  # distance from 1st city to the 1st city with station
    end_distance = abs(end - length + 1)  # distance from the ast city with station to the last city in path

    if start == 0 and end == length - 1:
        result = segments_max(stations)
    elif start == 0 and end != length - 1:
        result = segments_max(stations, end_distance)
    elif start != 0 and end == length - 1:
        result = segments_max(stations, start_distance)
    else:
        max_distance = max(abs(end - length + 1), abs(start - 0))
        result = segments_max(stations, max_distance)

    return result


print(flatlandSpaceStations(20, [0,4,12,16]))