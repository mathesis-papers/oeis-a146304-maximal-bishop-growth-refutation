# The OEIS maximal-bishop growth conjecture: an extension of Arshon's enumeration

Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

License: Creative Commons Attribution 4.0 International, `cc-by-4.0`.

## Main estimate

Let `a(n)` count inclusion-maximal nonattacking bishop subsets of the fixed-coordinate `n` by `n` board, without a rotation or reflection quotient. Let `A(n)` count all nonattacking subsets, including the empty subset, and let `B(j)` be the Bell number counting partitions of a `j`-element set.

For integers `n >= 3` and `1 <= t <= n-2`,

`t^(2(n-1-t)) <= a(n) <= A(n) <= min((n+1)(n!)^2, B(n+2)^2)`.

Extending Arshon's row-product enumeration (1936, pp. 25–29) to distinguishable maximal completions, the written proofs give

`log a(n) = log A(n) + o(n) = 2n(log n - log log n - 1) + O(n log log n / log n)`.

In particular, `a(n)^(1/(2n)) ~ n/(e log n)`, and `(a(n)/A(n))^(1/n) -> 1`. The latter does not assert `a(n)/A(n) -> 1`.

Each color count has the corresponding one-color estimate. The note also proves root estimates for the largest counting-polynomial coefficients, concentration at `2n-o(n)` bishops on the full board, vanishing fractions for fixed-`n` and maximum-size placements, and a degree-product lower bound for maximal matchings of a finite bipartite graph.

The parenthetical in A290613's name is corrected from “minimal edge covers” to “minimal vertex covers”: the 2 by 2 white bishop graph is one edge, with one minimal edge cover but two minimal vertex covers and two maximal independent sets. The sequence's maximal-independent-set counts are unchanged.

## Rebuild

Build the self-contained LaTeX source with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, run `pdflatex note.tex` twice. The bibliography is in the main source; no BibTeX step or external figure is needed.

Run the exact finite checks with Python 3.10 or newer:

```sh
python3 verify.py > verification.rebuilt.json
cmp verification.json verification.rebuilt.json
sha256sum -c MANIFEST.sha256
```

The checker uses exact integers. It enumerates maximal placements and their color coefficients for `1 <= n <= 8`; compares all color coefficients with Santos's Theorem 2.2 for `1 <= n <= 12`; checks the staircase/Stirling identity for 1 through 30 rows; checks nested diagonal sets for `2 <= n <= 200`; recovers seeds from 24 distinct maximal completions on the 5 by 5 board; checks the ratio arithmetic for `50 <= m <= 200`; and enumerates the two-vertex graph's cover families. All infinite conclusions have written proofs in the note.

## Scientific sources and formal scope

- The conjecture is formula line 12 of the official OEIS export, revision 35: https://raw.githubusercontent.com/oeis/oeisdata/847798eafedfc5f486a00619e2926cfdb6bf73f9/seq/A146/A146304.seq . The formula is unsigned; Paolo Bonzini is credited for the entry, not separately for this formula.
- Andrew Howroyd's 2017 color decomposition and maximal-placement algorithm: https://oeis.org/A146304/a146304.txt .
- S. E. Arshon, *Solution of one combinatorial problem*, Matematicheskoe Prosveshchenie, series 1, issue 8 (1936), 24–29: https://www.mathnet.ru/eng/mp694 . The complete issue is also available from the Moscow Center for Continuous Mathematical Education: https://www.mccme.ru/free-books/djvu/mp1/mp1-8.djvu (printed pages 24–29). The row-product rule is on p. 25, equations (1)–(2), with a proof in the editorial footnote; the cardinality expansion is on p. 26, and the bishop formulas are on pp. 27–29.
- Irving Kaplansky and John Riordan, *The problem of the rooks and its applications*, Duke Mathematical Journal 13 (1946), 259–268: https://doi.org/10.1215/S0012-7094-46-01324-5 .
- Robert W. Robinson, *Counting arrangements of bishops*, Lecture Notes in Mathematics 560 (1976), 198–214: https://doi.org/10.1007/BFb0097382 . This concerns fixed-`n` dominating placements and symmetry classes; Section 4 also gives the `2^n` maximum-size count.
- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, published December 15, 2025, Theorems 3–4, pp. 3–6: https://cs.uwaterloo.ca/journals/JIS/VOL28/Santos/santos3.pdf . Earlier version: arXiv:2411.16492v2 (August 13, 2025), Theorems 2.1–2.2, https://arxiv.org/abs/2411.16492v2 . The nonmaximal formulas credit Arshon and Kotěšovec; Santos's color names are exchanged relative to the black-corner convention here.
- Pinned Lean statements: https://github.com/the-omega-institute/trureturing/blob/549945461571e5d29c740b71d3b02651c85044f5/D5/S3/Combinatorics/Graph/Domination/BishopMaximalPlacementGrowth.lean .

In the linked Lean file, `count_lower_bound` gives `m^(6m) <= a(4m+1)` for natural `m`, `ratio_lower_bound` gives the multiplied exponential-ratio inequality for `m >= 50`, and `result` negates the positive-constant eventual Big-O assertion. `physical_cap` bounds the size of a maximal set by `2n-2` for `n >= 2`; `source_family_card` identifies the cap-filtered and native maximal-set counts. The parameterized all-board lower bound, Bell upper bound, logarithmic correction, coefficient and concentration results, and general bipartite-graph statement have written proofs in `note.tex`.

The coverage table distinguishes the conjecture actually stated by the source from unposed extensions. No additional problem identifiers are assigned to the latter.
