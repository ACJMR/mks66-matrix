from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [100,0,0]

m = new_matrix(0,0)
i = 0
while i < 450:
    add_edge(m,0+i,0+i,0,50+i,0+i,0)
    add_edge(m,50+i,0+i,0,50+i,50+i,0)
    add_edge(m,50+i,50+i,0,0+i,50+i,0)
    add_edge(m,0+i,50+i,0,0+i,0+i,0)
    i+=2

i = 0
while i < 450:
    add_edge(m,0+i,500-i,0,50+i,500-i,0)
    add_edge(m,50+i,500-i,0,50+i,450-i,0)
    add_edge(m,50+i,450-i,0,0+i,450-i,0)
    add_edge(m,0+i,450-i,0,0+i,500-i,0)
    i+=2

draw_lines(m,screen,color)


matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

matrix_mult(A,B)
print_matrix(A)
print_matrix(B)

matrix_mult(B,A)
print_matrix(A)
print_matrix(B)

ident(B)
print_matrix(B)

matrix_mult(B,A)
print_matrix(A)


save_extension(screen, 'img.png')
display(screen)
