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
    length = len(matrix[0])
    r = 0
    while r < length:
        print_row(matrix,r)
        r+=1
    print("\n")
    pass

def print_row(matrix,r):
    length = len(matrix)
    c = 0
    row = ""
    while c < length:
        row += str(matrix[c][r]) + " "
        c+=1
    print(row)
    pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    c = 0
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
    length = len(m2)
    c = 0

    while c < length:
        r = 0
        m2temp = [m2[c][0], m2[c][1], m2[c][2], m2[c][3]]
        #print(m2temp)

        while r < 4:
            m2[c][r] = dot(m1,m2temp,r)
            r+=1
        c+=1
    pass

def dot(v1,v2,n): # n is which row of the 4x4 matrix we are on
    return v1[0][n]*v2[0] + v1[1][n]*v2[1] + v1[2][n]*v2[2] + v1[3][n]*v2[3]


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
