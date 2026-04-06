import re
import math
import numpy as np

def parse_attractors(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract circles from SVG: <circle cx="..." cy="..." r="..." ... />
    # We'll treat cx and cy as raw dimensions or projected coordinates
    circles = re.findall(r'<circle cx="([\d\.]+)" cy="([\d\.]+)" r="([\d\.]+)"', content)
    
    attractors = []
    for cx, cy, r in circles:
        # Based on the gist theory, we'll map these 2D coordinates back to the orbifold
        # The SVG is 1200x900. Let's assume cx -> dim1, cy -> dim2 mapping
        d_x = int(float(cx))
        d_y = int(float(cy))
        
        # Combined dimension for orbifold mapping
        d_combined = d_x * 71 + d_y
        attractors.append({
            'cx': d_x,
            'cy': d_y,
            'r': float(r),
            'orb': (d_x % 71, d_y % 59, (d_x + d_y) % 47)
        })
    return attractors

def analyze_attractors(attractors):
    total = len(attractors)
    print(f"### J-Invariant Attractor Analysis")
    print(f"Total Wells Parsed: {total}")
    
    # Check for SSP Alignment in the orbifold projections
    SSP = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]
    ssp_hits = 0
    for a in attractors:
        if any(coord in SSP for coord in a['orb']):
            ssp_hits += 1
            
    print(f"SSP Alignment Hits: {ssp_hits} / {total} ({ssp_hits/total*100:.1f}%)")
    
    # Clustering: Unique cells
    unique_cells = len(set(a['orb'] for a in attractors))
    print(f"Unique Orbifold Cells: {unique_cells}")
    
    # Correlation with Monster Irreps (Smallest)
    # dim(V1) = 196883 maps to (0, 0, 0)
    origin_dist = [math.sqrt(sum(c**2 for c in a['orb'])) for a in attractors]
    avg_dist = sum(origin_dist) / total
    print(f"Average Distance from (0,0,0): {avg_dist:.2f}")

if __name__ == "__main__":
    attractors = parse_attractors('gists_content/cc55695b57b043b2092ac58967af51a4.txt')
    analyze_attractors(attractors)
