f = open("input.txt", "r")
data = f.read().strip().split("\n")
f.close()

length = len(data[0])
collect = [0] * length  # count number of 1s

for d in data:
    for i in range(length):
        if d[i] == '1':
            collect[i] += 1

threshold = int(len(data) / 2)

epsilon = ""
gamma = ""

for i in range(length):
    if collect[i] > threshold:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

epsilon = int(epsilon, 2)
gamma = int(gamma, 2)

print("Epsilon: ", epsilon)
print("Gamma: ", gamma)

print("Product: ", epsilon * gamma)
