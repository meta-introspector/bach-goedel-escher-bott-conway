from master_tree_encoding import OMEGA, SSP

def weave_holomorphic_tapestry():
    # Emoji Palette
    palette = {
        "LATTICE": "🕸️",
        "OMEGA": "🌑",
        "KERNEL": "⚙️",
        "HECKE": "🛠️",
        "VIRASORO": "🌀",
        "FROBENIUS": "💎",
        "DESCENT": "🪜",
        "FOURIER": "🌊",
        "CORPUS": "📜",
        "GALOIS": "🎭",
        "ORBIFOLD": "🔘"
    }
    
    # Mapping logic based on modular resonance
    def get_thread(n):
        res = OMEGA % n
        if n in SSP: return palette["LATTICE"]
        if n == 24: return palette["VIRASORO"]
        if n == 27: return palette["FROBENIUS"]
        if res == 0: return palette["KERNEL"]
        
        # Branch mapping from previous analysis
        branch_idx = res % 6
        branches = [
            palette["OMEGA"], palette["HECKE"], palette["CORPUS"], 
            palette["FOURIER"], palette["GALOIS"], palette["ORBIFOLD"]
        ]
        return branches[branch_idx]

    print("# THE HOLOMORPHIC TAPESTRY OF Ω")
    print("Generated from the modular weave of the 1-71 conformal index.\n")
    
    tapestry = []
    current_row = ""
    for n in range(1, 72):
        thread = get_thread(n)
        current_row += thread
        if n % 8 == 0:
            tapestry.append(current_row)
            current_row = ""
    if current_row:
        tapestry.append(current_row)
        
    for row in tapestry:
        print(row)
    
    print("\n## Tapestry Legend")
    print(" | ".join([f"{v} {k}" for k, v in palette.items()]))
    print("\n*The weave follows the stringy dimensional descent: 🪜 -> 💎 -> 🌀 -> 🕸️*")

if __name__ == "__main__":
    weave_holomorphic_tapestry()
