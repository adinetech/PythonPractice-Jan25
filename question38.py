## Matrix Transpose: Write a function to find the transpose of a given matrix (list of lists).

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_transpose(matrix))

if __name__ == "__main__":
    main()