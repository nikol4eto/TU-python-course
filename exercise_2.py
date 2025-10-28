
#A Python program that performs basic matrix operations like addition, subtraction, multiplication, and transpose.

def read_matrix(rows, cols, name="Matrix"):
    print(f"\nEnter values for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"  Row {i+1}: ").split()))
        if len(row) != cols:
            print("Each row must have exactly", cols, "numbers.")
            return read_matrix(rows, cols, name)
        matrix.append(row)
    return matrix


def print_matrix(matrix, title="Result"):
    print(f"\n {title}:")
    for row in matrix:
        print("  ", "  ".join(f"{num:7.2f}" for num in row))


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def multiply_matrices(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print("Available operations: add, subtract, multiply, transpose")

choice = input("Choose operation: ").strip().lower()

if choice in ("add", "subtract"):
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    A = read_matrix(r, c, "Matrix A")
    B = read_matrix(r, c, "Matrix B")
    if choice == "add":
        result = add_matrices(A, B)
    else:
        result = subtract_matrices(A, B)
    print_matrix(result, f"A {choice} B")

elif choice == "multiply":
    r1 = int(input("Rows in A: "))
    c1 = int(input("Columns in A: "))
    A = read_matrix(r1, c1, "Matrix A")

    r2 = int(input("Rows in B: "))
    c2 = int(input("Columns in B: "))
    if c1 != r2:
        print("Cannot multiply! Columns of A must equal rows of B.")
    else:
        B = read_matrix(r2, c2, "Matrix B")
        result = multiply_matrices(A, B)
        print_matrix(result, "A × B")

elif choice == "transpose":
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    A = read_matrix(r, c, "Matrix A")
    result = transpose_matrix(A)
    print_matrix(result, "Transpose of A")

else:
    print("Invalid operation. Try again.")
