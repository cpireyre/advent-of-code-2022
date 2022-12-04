def parse(line):
    l, r = line.strip().split(',')
    l, r = l.split('-'), r.split('-')
    return tuple([int(l[0]), int(l[1])]), tuple([int(r[0]), int(r[1])])

# Part I
def assignments_overlap(l, r):
    return (l[0] <= r[0] <= r[1] <= l[1]) or (r[0] <= l[0] <= l[1] <= r[1])

# Part II
def assignments_overlap2(l, r):
    return (l[0] <= r[0] <= l[1]) or (r[0] <= l[0] <= r[1]) or (l[0] <= r[1] <= l[1]) or (r[0] <= l[1] <= r[1])
    # GPT suggested: return min(l[1], r[1]) >= max(l[0], r[0]), kinda better 🙈

with open('4-input.txt', 'r') as f:
    # res = sum(assignments_overlap(*parse(l)) for l in f.readlines())
    res2 = sum(assignments_overlap2(*parse(l)) for l in f.readlines())

# print(res) # 556
print(res2) # 876
