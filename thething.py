#!/usr/bin/env python3
from dataclasses import dataclass

TABLE_HEIGHT = 10
TABLE_WIDTH = 10

@dataclass
class NumberPair:
    x: int
    y: int

the_table = []

#iterate over the rows
for row in range(TABLE_HEIGHT):
    the_table.append([])
    for column in range(TABLE_WIDTH):
        the_table[row].append(NumberPair(column,row))

for row in the_table:
    print("\n =============================== \n")
    print(row)
