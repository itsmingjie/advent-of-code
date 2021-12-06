f = open("input.txt", "r")
data = f.read().strip().split("\n")
f.close()

# parse data
data = [[[int(z) for z in y.split(",")] for y in x.split("->")] for x in data]

size = 1000

# 1000x1000 grid
grid = [[0 for x in range(size)] for y in range(size)]

for entry in data:
    # only consider when x1 = x2 or y1 = y2
    if entry[0][0] != entry[1][0] and entry[0][1] != entry[1][1]:
        continue
    
    # increment value of line from x1,y1 to x2,y2
    if entry[0][0] == entry[1][0]:
        x = entry[0][0]
        p_from = min(entry[0][1], entry[1][1])
        p_to = max(entry[0][1], entry[1][1])
        # x value the same, vertical line
        for y in range(p_from, p_to + 1):
            grid[y][x] += 1
    else:
        y = entry[0][1]
        p_from = min(entry[0][0], entry[1][0])
        p_to = max(entry[0][0], entry[1][0])
        # y value the same, horizontal line
        for x in range(p_from, p_to + 1):
            grid[y][x] += 1
    
# count number of points where more than one line is present
count = 0

for x in range(size):
    for y in range(size):
        if grid[x][y] > 1:
            count += 1

print(count)
