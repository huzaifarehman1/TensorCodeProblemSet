# The Ancient Sliding Puzzle

## Story

While exploring the ruins of an ancient civilization, archaeologists uncovered a mysterious sliding puzzle. The puzzle consists of numbered tiles and one empty space that allows the tiles to slide.

Over the centuries, many explorers have attempted to solve these puzzles. Some proudly recorded the sequence of moves they believed was the **shortest possible solution**. Unfortunately, not every explorer was correct—some took unnecessary detours, while others never reached the solved configuration at all.

Your job is to verify these historical records.

For every puzzle configuration and the corresponding sequence of moves, determine whether the sequence is **the shortest possible solution**.

If it is, output **1**.

Otherwise, output **0**.

---

## Puzzle Representation

Each puzzle is a **3 × 3 sliding puzzle** containing the numbers **1 to 8** and a single empty space represented by **0**.

The goal state is

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 0 |

The puzzle state is stored row-wise in the dataset.

For example,

| cell_0 | cell_1 | cell_2 | cell_3 | cell_4 | cell_5 | cell_6 | cell_7 | cell_8 |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 | 8 |

represents

```
1 2 3
4 5 6
7 0 8
```

---

## Move Encoding

The candidate solution is given as a sequence of digits.

Each digit represents a move of the empty tile.

| Value | Move |
|-------|------|
| 0 | Up |
| 1 | Down |
| 2 | Left |
| 3 | Right |

For example,

```
2301
```

means

- Left
- Right
- Up
- Down

---

## Move Definition

Each action represents the movement of the **empty tile (0)**.

| Value | Action | Description |
|-------|--------|-------------|
| 0 | Up | Move the empty tile one cell upward by swapping it with the tile directly above it. |
| 1 | Down | Move the empty tile one cell downward by swapping it with the tile directly below it. |
| 2 | Left | Move the empty tile one cell to the left by swapping it with the tile directly to its left. |
| 3 | Right | Move the empty tile one cell to the right by swapping it with the tile directly to its right. |

If an action would move the empty tile outside the board, that action is **invalid**.

___

## Task

For each puzzle:


1. Check whether the sequence successfully solves the puzzle.
2. Determine whether the sequence is the **shortest possible solution**.

Predict

- **1** if the sequence is the shortest possible solution.
- **0** otherwise.

A sequence is shortest possible solution if no sequence less than its length exists as a solution (solving the puzzle).  it may be that more than 1 shortest possible solutions exists all having the same shortest lengths
---

## Dataset

The  data consists of two files.

### `training_set.csv`

Contains the initial puzzle configurations.

### `test_set.csv`

Contains the candidate move sequence for each puzzle.


The file names are just default and its not the same paragim as machine learning.
### `task`

Your task is to predict the labels for each puzzle configuration (in training_set.csv) with its corresponding sequence (in test_set.csv) and if its the shortest solution for the puzzle configuration put **1** in its corresponding row in a new data file else put **0**.

---

## Output Format

Submit a CSV file in the following format.

|  target |
|--------|
|  1  |
|  0  |
|  1  |

where

- **1** indicates the provided sequence is the shortest possible solution.
- **0** indicates otherwise.
The CSV MUST HAVE A `target` COLUMN
---

## Evaluation

Your predictions will be evaluated using a classification metric such as:

- **Precision Score**

---

## Constraints

- Every puzzle is solvable.
- Candidate sequences may be valid or invalid.
- Candidate sequences may solve the puzzle but not optimally.
- Candidate sequences may contain illegal moves.
- Puzzle IDs are unique and dont have any influence on solution its just an indicator.