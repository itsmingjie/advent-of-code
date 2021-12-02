# Advent of Code 2021 - Day 1, Second Half
# https://adventofcode.com/2021/day/1

f = open("input.txt", "r")
depths = f.read().strip().split("\n")
depths = [int(x) for x in depths]
f.close()

count = 0

for i in range(len(depths) - 3):
    current_sum = depths[i + 1] + depths[i + 2] + depths[i + 3];
    prev_sum = depths[i] + depths[i + 1] + depths[i + 2];

    if (current_sum > prev_sum):
        count += 1

print(count)
