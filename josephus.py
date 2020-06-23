def josephus(items,k):
    final_arr = []
    k -= 1
    dead_guy_meme = k
    if len(items) == 0:
        return []
    if len(items) == 1:
        return items

    if dead_guy_meme > len(items):
        dead_guy_meme = dead_guy_meme % len(items)

    while len(items) > 1:
        final_arr.append(items[dead_guy_meme])
        items.pop(dead_guy_meme)
        dead_guy_meme = (dead_guy_meme + k) % len(items)

    final_arr.append(items[0])

    print(final_arr)
    #your code here
josephus([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],40)
