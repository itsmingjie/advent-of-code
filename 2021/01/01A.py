directions = ["forward", "down", "up"]
actions = [[1, 0], [0, 1], [0, -1]]

f = open("input.txt", "r")
inputs = f.read().strip().split("\n")
inputs = [x.split(" ") for x in inputs]
inputs = [[x[0], int(x[1])] for x in inputs]
f.close()

x, y = 0, 0

for (direction, distance) in inputs:
    index = directions.index(direction)
    x += actions[index][0] * distance
    y += actions[index][1] * distance

print(x, y)
print(x * y)
