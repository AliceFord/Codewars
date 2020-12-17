def blocks_to_collect(level):
    if level == 1: return {"total": 9, "gold": 9, "diamond": 0, "emerald": 0, "iron": 0}
    elif level == 2: return {"total": 34, "gold": 9, "diamond": 25, "emerald": 0, "iron": 0}
    elif level == 3: return {"total": 83, "gold": 9, "diamond": 25, "emerald": 49, "iron": 0}
    else: return {"total": 10, "gold": 9, "diamond": 25, "emerald": 49, "iron": 81}


print(blocks_to_collect(4))
