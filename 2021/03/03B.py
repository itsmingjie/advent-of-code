f = open("input.txt", "r")
data = f.read().strip().split("\n")
f.close()


def run_collect(dd, index):
    count = 0
    for d in dd:
        if d[index] == '1':
            count += 1

    return count


def run_filter(dd, index, is_mcv):
    if len(dd) == 1:
        return dd[0]

    count = run_collect(dd, index)

    threshold = len(dd) / 2
    mcv = '1' if count >= threshold else '0'
    lcv = '0' if count >= threshold else '1'

    vv = mcv if is_mcv else lcv

    i = 0
    while i < len(dd):
        if dd[i][index] != vv:
            del dd[i]
        else:
            i += 1

    return run_filter(dd, index + 1, is_mcv)


oxy = int(run_filter(data.copy(), 0, True), 2)
co2 = int(run_filter(data.copy(), 0, False), 2)

print("Oxy: ", oxy)
print("CO2: ", co2)

print("Product: ", oxy * co2)
