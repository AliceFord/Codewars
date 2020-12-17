def calc_fuel(n):
    ingot = 11 * n
    fuels = {"lava": 800, "blaze rod": 120, "coal": 80, "wood": 15, "stick": 1}
    ans = {"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}
    for key in fuels:
        ans[key] = ingot // fuels[key]
        ingot %= fuels[key]
    return ans

print(calc_fuel(37))
