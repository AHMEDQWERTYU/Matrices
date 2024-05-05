def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            element = int(input(f"Enter element ({i}, {j}): "))
            matrix[i].append(element)
    return matrix

def perform_addition(matrices):
    result = matrices[0]

    for i in range(1, len(matrices)):
        if len(matrices[i]) != len(result) or len(matrices[i][0]) != len(result[0]):
            print("Error")
            return
        for row in range(len(result)):
            for col in range(len(result[0])):
                result[row][col] += matrices[i][row][col]

    print("Result of addition:")
    print_matrix(result)

def perform_subtraction(matrices):
    result = matrices[0]

    for i in range(1, len(matrices)):
        if len(matrices[i]) != len(result) or len(matrices[i][0]) != len(result[0]):
            print("Error")
            return
        for row in range(len(result)):
            for col in range(len(result[0])):
                result[row][col] -= matrices[i][row][col]

    print("Result of subtraction:")
    print_matrix(result)

def perform_multiplication(matrices):
    if len(matrices) < 2:
        print("Error")
        return

    result = matrices[0]

    for i in range(1, len(matrices)):
        if len(result[0]) != len(matrices[i]) or not result or not matrices[i]:
            print("Error")
            return
        result = multiply_matrices(result, matrices[i])

    if not result:
        print("Error")
        return

    print("Result of multiplication:")
    print_matrix(result)

def multiply_matrices(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2 or rows1 == 0 or cols1 == 0 or cols2 == 0:
        return [[]]

    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    n_matrices = int(input("Enter the number of matrices: "))
    matrices = []
    for i in range(n_matrices):
        print(f"Matrix {i}:")
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        matrices.append(create_matrix(rows, cols))

    operation = input("Enter the operation you want to perform (addition, subtraction, multiplication): ").lower()

    if operation == "addition":
        perform_addition(matrices)
    elif operation == "subtraction":
        perform_subtraction(matrices)
    elif operation == "multiplication":
        perform_multiplication(matrices)
    else:
        print("Invalid operation!")
