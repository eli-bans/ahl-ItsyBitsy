# @ItsyBitsy
# a function to calculate the sum of the diagonals of a square matrix
def matrixDiagonal(mat):
    # if input is not a square matrix, return None
    if len(mat[0]) != len(mat):
        return None
    left = 0  # left pointer initialized to point to the first item in the array
    right = -1  # right pointer initialized to point to the last item in the array
    total = 0  # accounts for the sum of the diagonals of the matrix
    for i in range(len(mat)):
        # if pointers point to the same item, select one
        if mat[i][left] == mat[i][right]:
            total += mat[i][left]
        else:
            total += mat[i][left] + mat[i][right]
        left += 1
        right -= 1
    return total
