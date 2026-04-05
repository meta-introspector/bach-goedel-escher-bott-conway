def fractran_step(n, program):
    for num, den in program:
        if n % den == 0:
            return (n * num) // den
    return None

def run_simulation(index_limit=71):
    # Program A extracted from the gist
    # 50653/2197, 27/4, 19/41, 2197/289, 6859/19, 4913/289, 7/8, 2209/17
    program_a = [(50653, 2197), (27, 4), (19, 41), (2197, 289), (6859, 19), (4913, 289), (7, 8), (2209, 17)]
    
    print(f"| Initial (n) | FRACTRAN Path | Final State | Orbifold Resonance |")
    print(f"| :--- | :--- | :--- | :--- |")
    
    for n in range(1, index_limit + 1):
        path = [n]
        current = n
        steps = 0
        while steps < 10: # Limit steps for simulation
            next_n = fractran_step(current, program_a)
            if next_n is None or next_n in path: # Stop if no fraction applies or cycle
                break
            current = next_n
            path.append(current)
            steps += 1
        
        if len(path) > 1:
            o71, o59 = current % 71, current % 59
            dist = abs(o59 - o71) % 59
            resonance = "YES" if dist < 3 else "no"
            path_str = " -> ".join(map(str, path[:3])) + ("..." if len(path) > 3 else "")
            print(f"| {n} | {path_str} | {current} | {resonance} (dist={dist}) |")

if __name__ == "__main__":
    run_simulation(71)
