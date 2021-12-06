f = open("input.txt", "r")
data = f.read().strip().split("\n")
f.close()

# parse data
data = [[[int(z) for z in y.split(",")] for y in x.split("->")] for x in data]

size = 1000

# 1000x1000 grid
grid = [[0 for x in range(size)] for y in range(size)]

for entry in data:
    
    if entry[0][0] == entry[1][0]:
        x = entry[0][0]
        p_from = min(entry[0][1], entry[1][1])
        p_to = max(entry[0][1], entry[1][1])
        # x value the same, vertical line
        for y in range(p_from, p_to + 1):
            grid[y][x] += 1

    elif entry[0][1] == entry[1][1]:
        y = entry[0][1]
        p_from = min(entry[0][0], entry[1][0])
        p_to = max(entry[0][0], entry[1][0])
        # y value the same, horizontal line
        for x in range(p_from, p_to + 1):
            grid[y][x] += 1

    else:
        # 45 degrees diagonal line
        # get slope (-1 or 1)

        x_dir = 1 if entry[0][0] < entry[1][0] else -1
        y_dir = 1 if entry[0][1] < entry[1][1] else -1

        num_pts = abs(entry[1][0] - entry[0][0]) + 1

        x_from = entry[0][0]
        y_from = entry[0][1]

        for i in range(num_pts):
            x = x_from + i * x_dir
            y = y_from + i * y_dir
            
            grid[y][x] += 1

# count number of points where more than one line is present
count = 0

for x in range(size):
    for y in range(size):
        if grid[x][y] > 1:
            count += 1

print(count)
