import random
import numpy as np

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

def run_null_model(iterations=1000):
    program_a = [(50653, 2197), (27, 4), (19, 41), (2197, 289), (6859, 19), (4913, 289), (7, 8), (2209, 17)]
    
    # Original Data (1-71)
    original_resonances = 0
    for n in range(1, 72):
        final, changed = get_final_state(n, program_a)
        if changed:
            o71, o59 = final % 71, final % 59
            if (abs(o59 - o71) % 59) < 3:
                original_resonances += 1
    
    # Control Data (Random numbers)
    control_hits = []
    for _ in range(iterations):
        hits = 0
        random_inputs = [random.randint(1, 100000) for _ in range(71)]
        for val in random_inputs:
            final, changed = get_final_state(val, program_a)
            if changed:
                o71, o59 = final % 71, final % 59
                if (abs(o59 - o71) % 59) < 3:
                    hits += 1
        control_hits.append(hits)
    
    avg_control = sum(control_hits) / iterations
    std_control = np.std(control_hits)
    z_score = (original_resonances - avg_control) / std_control if std_control > 0 else 0
    
    print(f"### FRACTRAN Null Model Analysis")
    print(f"Original Resonance Hits (1-71): {original_resonances}")
    print(f"Expected Hits (Random Baseline): {avg_control:.2f} (std={std_control:.2f})")
    print(f"Significance (Z-score): {z_score:.2f}")
    
    if z_score > 2:
        print("RESULT: Significant signal detected (p < 0.05)")
    else:
        print("RESULT: Resonance within random noise parameters.")

if __name__ == "__main__":
    run_null_model(100)
