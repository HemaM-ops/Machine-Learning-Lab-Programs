
# M Hemasri - AIE22028
# ML Lab 1 programs
# Amrita School of Engineering, Bengaluru
#Program to perform the matrix multiplication

def matrix_mult(rowA,colA,rowB,colB,matA,matB):

    if colA==rowB:  #condition to check whether the matrices can be multiplied

        #initialize the resultant matrix to store the output
        result = [[0 for j in range(colB)] for i in range(rowA)]

        #matrix multiplication (multiplication operation)
        for i in range(len(matA)):
            for j in range(len(matB)):
                for k in range(len(matB)):
                    result[i][j] += matA[i][k] * matB[k][j]
    else:
        return "Matrices cannot be multiplied as columns of A is not equal to rows of B"

    return result



rows_A=int(input("Enter the number of rows in matrix A: "))
cols_A= int(input("Enter the number of columns in matrix A: "))

rows_B = int(input("\nEnter the number of rows in matrix B: "))
cols_B = int(input("Enter the number of columns in matrix B: "))

print("\nEntries for Matrix A: ")

matA= [[int(input(f" column {j+1} --> Enter {i+1} element: ")) for j in range(cols_A)] for i in range(rows_A) ]

print("\nEntries for Matrix B: ")
matB= [[int(input(f" column {j+1} --> Enter {i+1} element: ")) for j in range(cols_B)] for i in range(rows_B) ]


result_matrix = matrix_mult(rows_A,cols_A,rows_B,cols_B,matA,matB)


if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Resultant Matrix AB:")
    for row in result_matrix:
        print(row)
        


    


