import sys
import os

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
    if n < 2: return []
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

def get_arrows(n):
    factors = get_prime_factors(n)
    in_arrows = [f"{p}({HECKE_MAPPING.get(p, 'SSP')})" for p in factors if p in SSP]
    out_arrow = HECKE_MAPPING.get(n, "SSP" if n in SSP else "")
    return in_arrows, out_arrow

def analyze_file(file_path):
    print(f"\n### Conformal Analysis: {os.path.basename(file_path)}")
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # Paragraph level
    paragraphs = content.split(b'\n\n')
    offset = 0
    for pi, p in enumerate(paragraphs[:2]): # Limit to first 2
        in_arr, out_arr = get_arrows(offset)
        print(f"Para {pi} (offset {offset}): In={in_arr}, Out={out_arr}, Orb={get_orbifold_coords(offset)}")
        
        # Line level
        lines = p.split(b'\n')
        line_offset = offset
        for li, l in enumerate(lines[:2]): # Limit to first 2
            in_arr, out_arr = get_arrows(line_offset)
            print(f"  Line {li} (offset {line_offset}): In={in_arr}, Out={out_arr}")
            
            # Token level
            tokens = l.split()
            token_offset = line_offset
            for ti, t in enumerate(tokens[:3]): # Limit to first 3
                in_arr, out_arr = get_arrows(token_offset)
                print(f"    Token '{t.decode(errors='ignore')}' (offset {token_offset}): In={in_arr}, Out={out_arr}")
                
                # Char level (first char of token)
                if t:
                    char_offset = token_offset
                    char = t[0]
                    in_arr, out_arr = get_arrows(char_offset)
                    bits = bin(char)[2:].zfill(8)
                    print(f"      Char '{chr(char)}' (offset {char_offset}): Bits={bits}, In={in_arr}, Out={out_arr}")
                
                token_offset += len(t) + 1
            line_offset += len(l) + 1
        offset += len(p) + 2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        # Scan first few files in gists_content
        files = sorted(os.listdir('gists_content'))[:3]
        for f in files:
            if f.endswith('.txt') or f.endswith('.md'):
                analyze_file(os.path.join('gists_content', f))
