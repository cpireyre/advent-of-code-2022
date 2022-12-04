with open('1-input.txt') as snax:
    acc = 0
    total = []
    for snack in snax:
        calories = int(snack) if snack != "\n" else 0
        if calories > 0:
            acc += calories
        else:
            total += [acc]
            acc = 0
    total.sort(reverse=True)
    total += [0, 0, 0]
    print(total[0] + total[1] + total[2])
