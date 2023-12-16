import numpy as np
import sys

file = open(sys.argv[1])


def main(grid):
    for c in range(1, len(grid[0])):
        left_cols = grid[:, :c]
        right_cols = grid[:, c:]

        left_cols_len, right_cols_len = len(left_cols[0]), len(right_cols[0])

        size = min(left_cols_len, right_cols_len)

        if left_cols_len < right_cols_len:
            right_cols_inv = np.fliplr(right_cols)[:, right_cols_len - size :]
            if np.array_equal(left_cols, right_cols_inv):
                return c
        elif left_cols_len == right_cols_len:
            right_cols_inv = np.fliplr(right_cols)
            if np.array_equal(left_cols, right_cols_len):
                return c
        else:
            left_cols_inv = np.fliplr(left_cols)[:, :size]
            if np.array_equal(right_cols, left_cols_inv):
                return c

    for r in range(1, len(grid)):
        upper_rows = grid[:r]
        down_rows = grid[r:]

        upper_rows_len, down_rows_len = len(upper_rows), len(down_rows)

        size = min(upper_rows_len, down_rows_len)

        if upper_rows_len < down_rows_len:
            down_rows_inv = np.flipud(down_rows)[down_rows_len - size :]
            if np.array_equal(upper_rows, down_rows_inv):
                return 100 * (r)
        elif upper_rows_len == down_rows_len:
            down_rows_inv = np.flipud(down_rows)
            if np.array_equal(upper_rows, down_rows_len):
                return 100 * (r)
        else:
            upper_rows_inv = np.flipud(upper_rows)[:size]
            if np.array_equal(down_rows, upper_rows_inv):
                return 100 * (r)


result = 0

while True:
    grid = []
    line = file.readline()

    if not line:
        break

    while line != "\n" and line:
        grid.append(list(line.replace("\n", "")))

        line = file.readline()

    result += main(np.array(grid))

print(result)
