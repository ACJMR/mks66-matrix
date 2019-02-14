"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row0,row1,row2,row3 = "","","",""
    for x in matrix:
        row0 += str(x[0]) + " "
    for x in matrix:
        row1 += str(x[1]) + " "
    for x in matrix:
        row2 += str(x[2]) + " "
    for x in matrix:
        row3 += str(x[3]) + " "
    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print("")
    pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    c = 0
    r = 0
    length = len(matrix)
    while c < length:
        r = 0
        while r < length:
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
            r+=1
        c+=1

    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
