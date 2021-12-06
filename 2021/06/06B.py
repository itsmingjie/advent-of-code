f = open("input.txt", "r")
fish = f.read().strip().split(",")
f.close()

fish = [int(x) for x in fish]
days = [0] * 9

NUM_DAYS = 256

for i in range(len(fish)):
    days[fish[i]] += 1

for day in range(NUM_DAYS):

    num_spawns = days[0]

    for i in range(len(days) - 1):
        days[i] = days[i + 1]
    
    days[8] = num_spawns
    days[6] += num_spawns

print(sum(days))
