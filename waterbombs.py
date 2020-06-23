import math

def waterbombs(fire, w):
    pairs = []
    pair_count = 0
    bomb_count = 0
    if w == 1:
      return fire.count("x")

    for i in range(len(fire)):
        if fire[i] == "x":
            pair_count += 1
        if fire[i] == "Y" or i == len(fire)-1:
            pairs.append(pair_count)
            pair_count = 0

    for i in pairs:
        if i == 1:
            bomb_count += 1
        if i >= 2:
            bomb_count += math.ceil((i / w))

    return bomb_count

waterbombs("xxYxx", 3)
