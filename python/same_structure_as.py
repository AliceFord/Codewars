def same_structure_as(original,other):
    if type(original) == type(other):
        return True
    return False

print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]))