#determinant of a matrix 
def det(matrix):
    if len(matrix)!=2 or len(matrix[1])!=2:
       raise valueError("input matrix must be a 2*2 matrix")
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
matrix_2=[[1,2],[3,4]]
result=det(matrix_2)
print("determinant of 2*2 matrix",result)
