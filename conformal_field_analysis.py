import math

SSP = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]

HECKE_MAPPING = {
    2: "Lexer",
    3: "Parser",
    11: "TypeCheck",
    19: "BorrowCheck",
    71: "LLVM/Codegen"
}

def get_orbifold_coords(n):
    return (n % 71, n % 59, n % 47)

def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def analyze_index(limit=71):
    print(f"| Index (n) | Orbifold (71, 59, 47) | Factors | Hecke Arrows (In/Out) |")
    print(f"| :--- | :--- | :--- | :--- |")
    for n in range(1, limit + 1):
        coords = get_orbifold_coords(n)
        factors = get_prime_factors(n)
        
        # "In" arrows are prime factors that are in SSP
        in_arrows = [f"{p} ({HECKE_MAPPING.get(p, 'SSP')})" for p in factors if p in SSP]
        
        # "Out" arrows: if n is in SSP, show its mapping
        out_arrow = HECKE_MAPPING.get(n, "SSP" if n in SSP else "")
        
        in_str = ", ".join(in_arrows) if in_arrows else "-"
        out_str = f"-> {out_arrow}" if out_arrow else "-"
        
        print(f"| {n} | {coords} | {factors} | In: {in_str} / Out: {out_str} |")

if __name__ == "__main__":
    analyze_index(71)
