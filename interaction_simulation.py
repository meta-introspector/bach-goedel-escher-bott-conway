def fractran_step(n, program):
    if n <= 0: return None
    for num, den in program:
        if n % den == 0:
            return (n * num) // den
    return None

def get_final_state(n, program, max_steps=10):
    current = n
    path = [n]
    for _ in range(max_steps):
        next_n = fractran_step(current, program)
        if next_n is None or next_n in path:
            break
        current = next_n
        path.append(current)
    return current, len(path) > 1

def run_interaction_simulation(limit=71):
    program_a = [(50653, 2197), (27, 4), (19, 41), (2197, 289), (6859, 19), (4913, 289), (7, 8), (2209, 17)]
    
    results = []
    
    # n * n
    for n in range(1, limit + 1):
        val = n * n
        final, changed = get_final_state(val, program_a)
        if changed:
            o71, o59 = final % 71, final % 59
            dist = abs(o59 - o71) % 59
            if dist < 3:
                results.append(f"| n^2 | {n}^2={val} | {final} | YES (dist={dist}) |")

    # Sample n * m, n + m, n - m (using diagonal/selective sampling to keep output clean)
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]: # SSP Primes
        for m in [2, 3, 5, 7, 11, 13]: # Small SSP
            # n * m
            val = n * m
            final, changed = get_final_state(val, program_a)
            if changed:
                o71, o59 = final % 71, final % 59
                dist = abs(o59 - o71) % 59
                if dist < 3:
                    results.append(f"| n*m | {n}*{m}={val} | {final} | YES (dist={dist}) |")
            
            # n + m
            val = n + m
            final, changed = get_final_state(val, program_a)
            if changed:
                o71, o59 = final % 71, final % 59
                dist = abs(o59 - o71) % 59
                if dist < 3:
                    results.append(f"| n+m | {n}+{m}={val} | {final} | YES (dist={dist}) |")

            # n - m
            if n > m:
                val = n - m
                final, changed = get_final_state(val, program_a)
                if changed:
                    o71, o59 = final % 71, final % 59
                    dist = abs(o59 - o71) % 59
                    if dist < 3:
                        results.append(f"| n-m | {n}-{m}={val} | {final} | YES (dist={dist}) |")

    print("| Op | Input | Final State | Resonance |")
    print("| :--- | :--- | :--- | :--- |")
    for r in results[:30]: # Limit output lines
        print(r)

if __name__ == "__main__":
    run_interaction_simulation(71)
