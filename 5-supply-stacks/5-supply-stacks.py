# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 

stacks = {}
# stacks[1] = ['Z', 'N']
# stacks[2] = ['M', 'C', 'D']
# stacks[3] = ['P']

stacks[1] = ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T']
stacks[2] = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
stacks[3] = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
stacks[4] = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
stacks[5] = ['H', 'V', 'R', 'P', 'T', 'B']
stacks[6] = ['C', 'B', 'P', 'T']
stacks[7] = ['B', 'J', 'R', 'P', 'L']
stacks[8] = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
stacks[9] = ['L', 'S', 'G']

def parse(line):
    words = line.strip().split(' ')
    return int(words[1]), int(words[3]), int(words[5])

# this mutates the global object, this is very bad, etc
def move(amount, orig, to):
    for _ in range(amount):
        if stacks[orig]:
            stacks[to].append(stacks[orig].pop())

with open('5-input.txt', 'r') as f:
    for line in f.readlines():
        instructions = parse(line)
        # print(stacks)
        # print(instructions)
        move(*instructions)
        # print(stacks)


from pprint import pprint
pprint(stacks) # LJSVLTWQM
