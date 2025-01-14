## Matrix Addition: Prompt the user for two 2D matrices (lists of lists) of the same dimensions. Perform matrix addition and print the result.

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print(matrix_addition(matrix1, matrix2))

if __name__ == "__main__":
    main()