# The OEIS maximal-bishop growth conjecture: an extension of Arshon's enumeration

**Authors:** Haobo Ma, Wenlin Zhang

The formula at line 12 of the pinned official export of OEIS A146304, revision 35 (February 16, 2025), conjectures that the number a(n) of inclusion-maximal nonattacking bishop subsets of the fixed-coordinate n by n board is O(n^(n-1)); extending Arshon's enumeration (1936, pp. 25-29) to distinguishable maximal completions disproves this growth law. For integers n >= 3 and 1 <= t <= n-2, prescribing occupied difference diagonals and recovering the seeds from maximal extensions gives t^(2(n-1-t)) <= a(n), while a staircase-board embedding gives a(n) <= A(n) <= B(n+2)^2, where A(n) counts all nonattacking subsets and B(j) is the jth Bell number. Thus log(a(n)) and log(A(n)) equal 2n(log(n)-log(log(n))-1) + O(n log(log(n))/log(n)), and a(n)^(1/(2n)) is asymptotic to n/(e log(n)). Each color has the corresponding one-color estimate. The largest coefficients have the same root estimates, and the proportion of placements with fewer than (2-epsilon)n bishops tends to zero for every fixed epsilon > 0.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24487649](https://doi.org/10.5281/zenodo.24487649)
- Concept DOI: [https://doi.org/10.5281/zenodo.24487648](https://doi.org/10.5281/zenodo.24487648)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [oeis-a146304-maximal-bishop-growth-refutation](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a146304-maximal-bishop-growth-refutation?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). The OEIS maximal-bishop growth conjecture: an extension of Arshon's enumeration. Mathesis, version 2. https://doi.org/10.5281/zenodo.24487649

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Lemma (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Lemma (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
