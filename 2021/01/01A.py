# Advent of Code 2021 - Day 1, First Half
# https://adventofcode.com/2021/day/1

f = open("input.txt", "r")
depths = f.read().strip().split("\n")
depths = [int(x) for x in depths]
f.close()

count = 0

for i in range(len(depths) - 1):
    if (depths[i + 1] - depths[i]) > 0:
        count += 1

print(count)
