import heapq
import pandas as pd

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

GOAL_POS = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1)
}

# 0 = Up
# 1 = Down
# 2 = Left
# 3 = Right
MOVES = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}


def manhattan(state):
    h = 0
    for idx, tile in enumerate(state):
        if tile == 0:
            continue
        r, c = divmod(idx, 3)
        gr, gc = GOAL_POS[tile]
        h += abs(r - gr) + abs(c - gc)
    return h


def astar(start):
    """
    Returns optimal number of moves from start to GOAL.
    """

    if start == GOAL:
        return 0

    pq = []

    g_cost = {start: 0}

    heapq.heappush(
        pq,
        (manhattan(start), 0, start)
    )

    while pq:

        f, g, state = heapq.heappop(pq)

        if state == GOAL:
            return g

        if g > g_cost[state]:
            continue

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in MOVES.values():

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
                continue

            nz = nr * 3 + nc

            nxt = list(state)
            nxt[zero], nxt[nz] = nxt[nz], nxt[zero]
            nxt = tuple(nxt)

            ng = g + 1

            if nxt not in g_cost or ng < g_cost[nxt]:
                g_cost[nxt] = ng
                nf = ng + manhattan(nxt)
                heapq.heappush(
                    pq,
                    (nf, ng, nxt)
                )

    return -1


def check_sequence(board, sequence):
    """
    Returns:
        valid (bool)
        moves_used (int)
    """

    board = list(board)

    sequence = str(sequence)

    for ch in sequence:

        if ch not in "0123":
            return False, 0

        move = int(ch)

        zero = board.index(0)
        r, c = divmod(zero, 3)

        dr, dc = MOVES[move]

        nr = r + dr
        nc = c + dc

        if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
            return False, 0

        nz = nr * 3 + nc

        board[zero], board[nz] = board[nz], board[zero]

    return tuple(board) == GOAL, len(sequence)


def main():
    path1 = ''
    path2 = ''
    puzzles = pd.read_csv(path1)
    sequences = pd.read_csv(path2)

    # assumes sequence is the last column
    seq_col = 'sequence'

    targets = []

    for (_, p_row), (_, s_row) in zip(
            puzzles.iterrows(),
            sequences.iterrows()):

        board = tuple(p_row.iloc[-9:].tolist())

        sequence = str(s_row[seq_col])

        solved, used = check_sequence(board, sequence)

        if not solved:
            targets.append(0)
            continue

        optimal = astar(board)

        if used == optimal:
            targets.append(1)
        else:
            targets.append(0)

    submission = pd.DataFrame({
        "target": targets
    })

    submission.to_csv("submission.csv", index=False)

    print("submission.csv created successfully.")


if __name__ == "__main__":
    main()