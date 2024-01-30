
# M Hemasri - AIE22028
# ML Lab 1 programs
# Amrita School of Engineering, Bengaluru
#Program to find the transpose of a matrix


def transpose(matA,rows,cols):
    #initialize matrix B to store the transpose of A
    B = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            B[i][j]=matA[j][i]


    return B

rows_A=int(input("Enter the number of rows in matrix A: "))
cols_A= int(input("Enter the number of columns in matrix A: "))

print("\nEntries for Matrix A: ")

matA= [[int(input(f" column {j+1} --> Enter {i+1} element: ")) for j in range(cols_A)] for i in range(rows_A) ]

matB= transpose(matA,rows_A,cols_A)

 
print("Result matrix is: ") 
for i in range(cols_A): 
 for j in range(rows_A): 
  print(matB[i][j], " ", end='') 
 print()
