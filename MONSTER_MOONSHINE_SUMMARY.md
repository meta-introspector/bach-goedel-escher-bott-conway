# Monster Moonshine & FRACTRAN: Constants and Formulas Summary

This document summarizes the mathematical constants, formulas, and relationships extracted from the `gists_content/` directory.

## 1. Key Constants

### Monster Group & Modular Forms
| Constant | Value | Description |
| :--- | :--- | :--- |
| **Supersingular Primes (SSP)** | `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71` | The 15 primes that divide the order of the Monster group. |
| **Monster Group Order (|M|)** | $\approx 8.08 \times 10^{53}$ | $2^{46} \cdot 3^{20} \cdot 5^9 \cdot 7^6 \cdot 11^2 \cdot 13^2 \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 \cdot 41 \cdot 47 \cdot 59 \cdot 71$ |
| **Moonshine Constant** | `744` | The constant term ($c_0$) in the Fourier expansion of the $j$-invariant. |
| **Monster Orbifold Volume** | `196,883` | The dimension of the smallest non-trivial irreducible representation. |
| **Orbifold Grid Bases** | `71, 59, 47` | Prime bases used for 3D coordinate mapping. |

### McKay-Thompson Coefficients ($j_n$)
| Coefficient | Value | Relation to Monster Irreps |
| :--- | :--- | :--- |
| **$j_1$** | `196,884` | $1 + 196,883$ (Trivial + 1st non-trivial irrep) |
| **$j_2$** | `21,493,760` | $1 + 196,883 + 21,296,876$ (Sum of first 3 irreps) |
| **$j_3$** | `864,299,970` | Sum of specific irrep dimensions. |

---

## 2. Core Formulas

### 1. Orbifold Coordinate Mapping
Maps a scalar $n$ to 3D space using the largest SSP primes:
$$f(n) = (n \pmod{71}, n \pmod{59}, n \pmod{47})$$

### 2. Complex Modularity Parameter ($\tau$)
Used in the calculation of $j$-invariant attractors:
$$\tau = \frac{o71 + i \cdot o59}{o47}$$

### 3. j-Invariant q-Expansion (Monstrous Moonshine)
The deep connection between the Monster group and modular forms:
$$j(\tau) = \frac{1}{q} + 744 + 196884q + 21493760q^2 + \dots$$
where $q = \exp(2\pi i \tau)$.

### 4. FRACTRAN Execution Logic
A FRACTRAN program is a list of fractions $\frac{N_1}{D_1}, \frac{N_2}{D_2}, \dots$. For an input $n$:
1. Find the first fraction where $D_i$ divides $n$.
2. Update $n \leftarrow n \cdot \frac{N_i}{D_i}$.
3. Repeat until no fraction applies.

---

## 3. Key Factorizations

*   **Smallest Monster Rep:** $196,883 = 47 \times 59 \times 71$
*   **Second Monster Rep:** $21,296,876 = 2^2 \times 31 \times 41 \times 59 \times 71$
*   **First Moonshine Coefficient (minus 744):** $21,493,760 = 2^{11} \times 5 \times 2,099$

---

## 4. Technical Mapping (Hecke Operators)
In the visualized system, Rust compiler stages are mapped to Hecke operators:
*   **$T_2 \to$ Lexer**
*   **$T_3 \to$ Parser**
*   **$T_{11} \to$ TypeCheck** ($\lambda_{11} \approx 1.075$)
*   **$T_{19} \to$ BorrowCheck**
*   **$T_{71} \to$ LLVM/Codegen**
