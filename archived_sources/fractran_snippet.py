def fractran(program, n, max_steps=1000):
    history = [n]
    for _ in range(max_steps):
        for num, den in program:
            if (n * num) % den == 0:
                n = (n * num) // den
                history.append(n)
                break
        else:
            break
    return history

# Reference Program: Conway's Prime Game
prime_game = [(17, 91), (78, 85), (19, 51), (23, 38), (29, 33), (77, 29), (95, 23), (77, 19), (1, 17), (11, 13), (13, 11), (15, 14), (15, 2), (55, 1)]
