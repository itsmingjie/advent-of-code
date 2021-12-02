f = open("input.txt", "r")
inputs = f.read().strip().split("\n")
inputs = [x.split(" ") for x in inputs]
inputs = [[x[0], int(x[1])] for x in inputs]
f.close()

x, y, aim = 0, 0, 0

for (direction, distance) in inputs:
    if (direction == "forward"):
        x += distance
        y += aim * distance
    elif (direction == "down"):
        aim += distance
    elif (direction == "up"):
        aim -= distance

print(x, y)
print(x * y)
