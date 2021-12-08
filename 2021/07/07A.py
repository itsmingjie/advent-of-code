f = open("input.txt", "r")
crabs = f.read().strip().split(",")
f.close()

crabs = [int(crab) for crab in crabs]

locations = [0] * (max(crabs) + 1)
costs = [0] * (max(crabs) + 1)

for crab in crabs:
    locations[crab] += 1

cheapest_index, cheapest_cost = 0, len(locations) ** 2

for i in range(len(locations)):
    cost = 0
    
    for j in range(len(locations)):
        if i != j:
            cost += abs(j - i) * locations[j]

    costs[i] = cost

    if cost < cheapest_cost:
        cheapest_index, cheapest_cost = i, cost

print(cheapest_index, cheapest_cost)
