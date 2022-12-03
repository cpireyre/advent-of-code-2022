ALPHA = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def split(rucksack):
    length = len(rucksack)
    return (set(rucksack[:length//2]), set(rucksack[length//2:]))

def common_item(left, right):
    return (left & right).pop()

def priority(c):
    # print(c)
    # print(ALPHA.index(c))
    return ALPHA.index(c)

test1 = "vJrwpWtwJgWrhcsFMMfFFhFp"

with open("3-input.txt", 'r') as f:
    lines = f.readlines()
    res = sum(priority(common_item(*(split(l)))) for l in lines)
    # print(res)
    # = 7821
