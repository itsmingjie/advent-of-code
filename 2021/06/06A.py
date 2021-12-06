f = open("input.txt", "r")
fish = f.read().strip().split(",")
f.close()

fish = [int(x) for x in fish]

NUM_DAYS = 80

for day in range(NUM_DAYS):
    for i in range(len(fish)):
        if fish[i] > 0:
            fish[i] -= 1
        else: 
            fish[i] = 6
            fish.append(8)

print(len(fish))
