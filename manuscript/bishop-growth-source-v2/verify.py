import json
from math import comb, factorial


REFERENCE_COUNTS = [1, 4, 10, 64, 660, 7744, 111888, 1960000]
REFERENCE_ALL = [2, 9, 70, 729, 9918, 167281, 3423362, 82609921]
REFERENCE_MAXIMAL_COLOR = {
    0: [[1], [2], [1, 4], [0, 4, 4], [0, 0, 22, 8],
        [0, 0, 16, 64, 8], [0, 0, 6, 128, 228, 16],
        [0, 0, 0, 72, 784, 528, 16]],
    1: [[1], [2], [0, 2], [0, 4, 4], [0, 2, 16, 4],
        [0, 0, 16, 64, 8], [0, 0, 0, 128, 160, 8],
        [0, 0, 0, 72, 784, 528, 16]],
}


def attacks(first, second):
    return first != second and (
        first[0] - first[1] == second[0] - second[1]
        or first[0] + first[1] == second[0] + second[1]
    )


def maximal_placements(cells):
    compatible = []
    for first_index, first in enumerate(cells):
        compatible.append(sum(
            1 << second_index
            for second_index, second in enumerate(cells)
            if first_index != second_index and not attacks(first, second)
        ))

    def enumerate_cliques(chosen, candidates, excluded):
        if candidates == 0 and excluded == 0:
            yield tuple(cells[index] for index in chosen)
            return
        union = candidates | excluded
        pivot = max(
            (index for index in range(len(cells)) if union & (1 << index)),
            key=lambda index: (compatible[index] & candidates).bit_count(),
        )
        branches = candidates & ~compatible[pivot]
        while branches:
            bit = branches & -branches
            index = bit.bit_length() - 1
            yield from enumerate_cliques(
                chosen + (index,),
                candidates & compatible[index],
                excluded & compatible[index],
            )
            candidates &= ~bit
            excluded |= bit
            branches &= ~bit

    yield from enumerate_cliques((), (1 << len(cells)) - 1, 0)


def diagonal_lines(size, color):
    differences = [
        difference for difference in range(1 - size, size)
        if difference % 2 == color
    ]
    differences.sort(key=lambda difference: (size - abs(difference), difference))
    return [
        [(row, row - difference) for row in range(size)
         if 0 <= row - difference < size]
        for difference in differences
    ]


def seeds_on_lines(lines):
    def extend(index, cells, used_sums):
        if index == len(lines):
            yield tuple(cells)
            return
        for cell in lines[index]:
            diagonal_sum = sum(cell)
            if diagonal_sum not in used_sums:
                yield from extend(index + 1, cells + [cell], used_sums | {diagonal_sum})

    yield from extend(0, [], set())


def maximal_completion(size, seed):
    placement = list(seed)
    for row in range(size):
        for column in range(size):
            cell = (row, column)
            if cell not in placement and all(not attacks(cell, other) for other in placement):
                placement.append(cell)
    return tuple(sorted(placement))


def all_coefficients(lines):
    states = {0: 1}
    for line in lines:
        following = dict(states)
        for used_sums, count in states.items():
            for cell in line:
                bit = 1 << sum(cell)
                if not used_sums & bit:
                    updated = used_sums | bit
                    following[updated] = following.get(updated, 0) + count
        states = following
    coefficients = [0] * (len(lines) + 1)
    for used_sums, count in states.items():
        coefficients[used_sums.bit_count()] += count
    return coefficients


def stirling_table(maximum):
    table = [[0] * (maximum + 1) for index in range(maximum + 1)]
    table[0][0] = 1
    for size in range(1, maximum + 1):
        for blocks in range(1, size + 1):
            table[size][blocks] = table[size - 1][blocks - 1] + blocks * table[size - 1][blocks]
    return table


def main():
    rows = []
    polynomials = []
    stirling = stirling_table(32)
    bell = [sum(row) for row in stirling]
    for size, expected in enumerate(REFERENCE_COUNTS, start=1):
        color_counts = []
        color_polynomials = []
        all_color_counts = []
        for color in range(2):
            cells = [(row, column) for row in range(size) for column in range(size)
                     if (row - column) % 2 == color]
            count = 0
            histogram = [0] * (size + 1)
            for placement in maximal_placements(cells):
                assert all(not attacks(first, second) for first in placement for second in placement)
                assert all(cell in placement or any(attacks(cell, other) for other in placement)
                           for cell in cells)
                count += 1
                histogram[len(placement)] += 1
                if size >= 2:
                    assert len(placement) <= size - 1
            if size >= 2:
                assert histogram[1:size] == REFERENCE_MAXIMAL_COLOR[color][size - 1]
            all_polynomial = all_coefficients(diagonal_lines(size, color))
            all_count = sum(all_polynomial)
            assert count <= all_count <= bell[size + 2]
            color_polynomials.append({'color': color, 'maximal': histogram,
                                      'all': all_polynomial})
            all_color_counts.append(all_count)
            color_counts.append(count)
        observed = color_counts[0] * color_counts[1]
        assert observed == expected
        assert all_color_counts[0] * all_color_counts[1] == REFERENCE_ALL[size - 1]
        assert observed <= (size + 1) * factorial(size) ** 2
        for omitted in range(1, size - 1):
            assert omitted ** (2 * (size - 1 - omitted)) <= observed
        rows.append({'n': size, 'difference_even': color_counts[0],
                     'difference_odd': color_counts[1], 'a_n': observed,
                     'all_n': all_color_counts[0] * all_color_counts[1]})
        polynomials.append({'n': size, 'color_polynomials': color_polynomials})

    for size in range(1, 13):
        for color in range(2):
            observed = all_coefficients(diagonal_lines(size, color))
            upper_binomial = (size + 1) // 2 if color == 0 else size // 2
            for bishops in range(size + 1):
                expected = sum(comb(upper_binomial, index) * stirling[size - index][size - bishops]
                               for index in range(min(bishops, upper_binomial) + 1))
                coefficient = observed[bishops] if bishops < len(observed) else 0
                assert coefficient == expected
            assert sum(observed) <= bell[size + 2]

    staircase = [1]
    for size in range(1, 31):
        following = [0] * (size + 1)
        for bishops in range(size + 1):
            if bishops < len(staircase):
                following[bishops] += staircase[bishops]
            if bishops:
                following[bishops] += (size - bishops + 1) * staircase[bishops - 1]
            assert following[bishops] == stirling[size + 1][size + 1 - bishops]
        staircase = following
        assert sum(staircase) == bell[size + 1]

    for size in range(2, 201):
        for color in range(2):
            lines = diagonal_lines(size, color)
            assert len(lines) >= size - 1
            for index, line in enumerate(lines):
                assert index <= len(line) <= index + 2
                assert len({sum(cell) for cell in line}) == len(line)
                assert all((cell[0] - cell[1]) % 2 == color for cell in line)
                if index:
                    assert {sum(cell) for cell in lines[index - 1]} <= {sum(cell) for cell in line}

    size = 5
    prescribed = [diagonal_lines(size, color)[1:4] for color in range(2)]
    seed_families = [list(seeds_on_lines(lines)) for lines in prescribed]
    completions = set()
    for even_seed in seed_families[0]:
        for odd_seed in seed_families[1]:
            seed = even_seed + odd_seed
            completion = maximal_completion(size, seed)
            assert all(not attacks(first, second) for first in completion for second in completion)
            assert completion not in completions
            completions.add(completion)
            occupied_differences = {row - column for row, column in seed}
            recovered = {cell for cell in completion if cell[0] - cell[1] in occupied_differences}
            assert recovered == set(seed)
            assert all(cell in completion or any(attacks(cell, other) for other in completion)
                       for row in range(size) for column in range(size) for cell in [(row, column)])

    for parameter in range(50, 201):
        assert 4 * (5 * parameter) ** 4 <= parameter ** 6
        assert 4 ** parameter * (4 * parameter + 1) ** (4 * parameter) <= parameter ** (6 * parameter)

    white_cells = [(0, 1), (1, 0)]
    assert attacks(*white_cells)
    maximal_independent_count = len(list(maximal_placements(white_cells)))
    assert maximal_independent_count == 2
    white_edges = [tuple(white_cells)]
    vertex_subsets = [frozenset(cell for index, cell in enumerate(white_cells) if mask & (1 << index))
                      for mask in range(1 << len(white_cells))]
    vertex_covers = [cover for cover in vertex_subsets
                     if all(first in cover or second in cover for first, second in white_edges)]
    minimal_vertex_covers = [cover for cover in vertex_covers
                             if not any(other < cover for other in vertex_covers)]
    edge_subsets = [frozenset(edge for index, edge in enumerate(white_edges) if mask & (1 << index))
                    for mask in range(1 << len(white_edges))]
    edge_covers = [cover for cover in edge_subsets
                   if set().union(*(set(edge) for edge in cover)) == set(white_cells)]
    minimal_edge_covers = [cover for cover in edge_covers
                           if not any(other < cover for other in edge_covers)]
    assert len(minimal_vertex_covers) == 2 and len(minimal_edge_covers) == 1

    result = {
        'arithmetic': 'exact integers; no floating-point arithmetic',
        'enumeration_method': 'maximal cliques of the nonattacking relation, separately on the two colors',
        'reference_url': 'https://raw.githubusercontent.com/oeis/oeisdata/847798eafedfc5f486a00619e2926cfdb6bf73f9/seq/A146/A146304.seq',
        'counts': rows,
        'coefficient_tables': polynomials,
        'coefficient_sources': ['https://oeis.org/A288183', 'https://oeis.org/A288182',
                                'https://arxiv.org/abs/2411.16492v2'],
        'all_coefficient_formula_range': {'n_min': 1, 'n_max': 12, 'colors': [0, 1],
                                          'statement': 'Santos Theorem 2.2 with the black-corner color convention'},
        'staircase_identity_range': {'rows_min': 1, 'rows_max': 30,
                                    'statement': 'R(m,k)=S(m+1,m+1-k) and total=B(m+1)'},
        'diagonal_profile_range': {'n_min': 2, 'n_max': 200, 'colors': [0, 1]},
        'completion_injection': {'n': 5, 'omitted_lines_per_color': 1,
                                 'seeds_per_color': [len(family) for family in seed_families],
                                 'distinct_maximal_completions': len(completions)},
        'ratio_arithmetic_range': {'m_min': 50, 'm_max': 200},
        'terminology_counterexample': {
            'source': 'https://raw.githubusercontent.com/oeis/oeisdata/847798eafedfc5f486a00619e2926cfdb6bf73f9/seq/A290/A290613.seq',
            'source_line': 5, 'n': 2, 'white_graph': 'K2',
            'maximal_independent_sets': maximal_independent_count,
            'minimal_vertex_covers': len(minimal_vertex_covers),
            'minimal_edge_covers': len(minimal_edge_covers),
        },
        'scope': 'Exact finite checks of maximal and all-subset counts, color coefficients, nested diagonal sets, staircase counts, seed recovery, and integer inequalities; the asymptotic conclusions have written proofs in note.tex.',
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
