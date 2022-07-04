def guass_jordan(matrix):
    stop = False
    n = len(matrix)  # number of rows in matrix
    m = len(matrix[0])  # number of columns in matrix
    for i in range(n):  # we check the numbers on the diagonal
        if matrix[i][i] == 0:  # if zero pivot
            c = 1
            # we want to find a row below the current row to switch with the current row
            # so that after the switch, we would not have 0 in this position on the diagonal anymore
            while i + c < n and matrix[i + c][i] == 0:
                c += 1
            # If we ran out of rows to switch out the 0, we break the loop
            if i + c == n:
                stop = True
                break
            # If we have indeed found a row to switch, we switch the two rows
            for k in range(m):
                matrix[i][k], matrix[i + c][k] = matrix[i + c][k], matrix[i][k]

        for j in range(n):
            if i != j:
                ratio = (
                    matrix[j][i] / matrix[i][i]
                )  # finding the ratio between a row directly above or below the diagonal and the diagonal for a given i
                for k in range(m):
                    matrix[j][k] = (
                        matrix[j][k] - (matrix[i][k]) * ratio
                    )  # subtracting off from that row so that matrix[j][i] is zero
    if stop:
        for i in range(n):
            sum = 0
            for j in range(n):
                sum = sum + matrix[i][j]
            if sum == matrix[i][j]:
                print("infinite solution")
                return
        print("no solution")
        return
    print(matrix)
    for i in range(n):
        print(matrix[i][m - 1] / matrix[i][i])


if __name__ == "__main__":
    matrix = [
        [0, 2, 1, 4],  # 2y + z = 4
        [1, 1, 2, 6],  # x + y + 2z = 6
        [2, 1, 1, 7],
    ]  # 2x + y + z = 7
    guass_jordan(matrix)

    # result:
    #   [[1.0, 0.0, 0.0, 2.2],
    #   [0.0, 2.0, 0.0, 2.8],
    #   [0.0, 0.0, -2.5, -3.0]]
    # 2.2
    # 1.4
    # 1.2

    matrix = [[2, 4, -2, -10], [3, 6, 0, -12]]  # 2x + 4y - 2z = -10  # 3x + 6y = -12
    guass_jordan(matrix)

    # result:
    # infinite solutions
