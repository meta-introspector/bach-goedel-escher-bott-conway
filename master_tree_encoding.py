import hashlib

def get_hash_int(s):
    # Returns a stable 10-bit integer from a string or number
    return int(hashlib.md5(str(s).encode()).hexdigest(), 16) % 1024

# System Components
SSP = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]
ORB_BASES = [71, 59, 47]
HECKE = {2: "Lexer", 3: "Parser", 11: "TypeCheck", 19: "BorrowCheck", 71: "LLVM"}
KERNEL = [(50653, 2197), (27, 4), (19, 41), (7, 8)]

# Source Archive Signatures
ARCHIVE_SIGNATURES = {'monster_dims_partial.txt': 0, 'BIBLIOGRAPHY.md': 830, 'fractran_snippet.py': 22, 'lean_modular_form.lean': 667}

# Node format: (Label, [Children/Values])
lattice_node = ("Lattice", [sum(SSP), sum(ORB_BASES)])
operator_node = ("Operators", [len(HECKE), sum(f[0] for f in KERNEL)])
corpus_node = ("Corpus", [20]) # 20 Gists
archive_node = ("Archive", list(ARCHIVE_SIGNATURES.values()))

def encode_tree(node):
    label, children = node
    # Prime power encoding: p1^hash(label) * p2^hash(child1) * p3^hash(child2) ...
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    val = get_hash_int(label)
    encoded = pow(primes[0], val)
    
    for i, child in enumerate(children):
        if isinstance(child, tuple):
            child_val = get_hash_int(encode_tree(child)) # Hash sub-tree to prevent explosion
        else:
            child_val = child
        
        # Use prime exponentiation for the child value
        encoded *= pow(primes[i+1], child_val % 128) # Keep exponents small (mod 128)
        
    return encoded

# Master Number Omega
system_tree = ("MonsterSystem", [lattice_node, operator_node, corpus_node, archive_node])
OMEGA = encode_tree(system_tree)

def traverse_system(omega, limit=71):
    print(f"| Step (n) | Resonance (Ω mod n) | Target Branch | Action / Interpretation |")
    print(f"| :--- | :--- | :--- | :--- |")
    
    branches = {
        0: "Lattice Core",
        1: "Operator Bridge",
        2: "Corpus Shard",
        3: "Kernel Flux",
        4: "Hecke Horizon"
    }
    
    for n in range(1, limit + 1):
        res = omega % n
        branch_idx = res % 5
        branch = branches[branch_idx]
        
        # Interpretation
        interpretation = "-"
        if n in SSP:
            interpretation = f"**SSP LOCK: Resonance at {n}**"
        elif res == 0:
            interpretation = "KERNEL ALIGNMENT"
            
        print(f"| {n} | {res} | {branch} | {interpretation} |")

if __name__ == "__main__":
    print(f"System Encoded. Master Number Ω has {len(str(OMEGA))} digits.")
    traverse_system(OMEGA, 71)
