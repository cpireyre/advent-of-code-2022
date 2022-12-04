# Part I:

ALPHA = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def split(rucksack):
#     global SCORE
#     length = len(rucksack)
#     return (set(rucksack[:length//2]), set(rucksack[length//2:]))

# def common_item(left, right):
#     return (left & right).pop()

def priority(c):
    # print(c)
    # print(ALPHA.index(c))
    return ALPHA.index(c)
# APPLE_SYMBOL = "@"
# SNAKE_SYMBOL = "&"
# test1 = "vJrwpWtwJgWrhcsFMMfFFhFp"

# with open("3-input.txt", 'r') as f:
#     lines = f.readlines()
#     res = sum(priority(common_item(*(split(l)))) for l in lines)
    # print(res)
    # = 7821

# Part II:

# I couldn't be bothered chunking things into 3-tuples on this end since
# that's very annoying to do with Python, and GPT deceived me by giving me
# incorrect code for that, so I just used qaJJjq200@a in Vim to chunk the
# input file directly lmao

def split(line):
    return line.strip().split(' ')

def badge(l, m, r):
    return (set(l) & set(m) & set(r)).pop()

with open("3-input.txt", 'r') as f:
    lines = f.readlines()
    res = sum(priority(badge(*(split(l)))) for l in lines)
    print(res) # 2752
    # for line in lines:
    #     trips = split(line)
    #     print(trips)
    #     print(badge(*trips))
