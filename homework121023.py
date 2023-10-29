'''
EXERCISE 3.2
Ignore First values in Answer 1&2!!!!!!!!
By @Edikscrmp, Sukharev Eduard, ID=522413990007
'''
import numpy as np

pansw=int
points = np.array([[1,1]])
interpoansw=[]
eqsppoint=np.linspace(-5, 5, 15)
lagrpoansw=[]
#Functions-------------------------------
def func(x):
    pansw = (1/(1+x**2))
    return pansw

def linear_interpolation( pointL, pointR, xi ):
    y = (xi-pointL[0])/(pointR[0]-pointL[0])*pointL[1] + (xi-pointR[0])/(pointL[0]-pointR[0])*pointR[1]
    return y

def piecewiselinear_interploation(points,xi):
    n = len(points)
    for k in range(n-1):
        if ( points[k,0] <= xi and xi <= points[k+1,0]):
            yi = linear_interpolation( points[k], points[k+1], xi )
            break
    return yi

def lagrange_interpolation(points, x):
    n = len(points)
    y = 0
    for i in range(n):
        term = points[i, 1]
        for j in range(n):
            if ( j != i ):
                term = term * ( x - points[j,0] ) / ( points[i,0] - points[j,0] )
        y = y + term
    return y

#---------------------------------------------------
for i in eqsppoint:
    new_row=np.array([i,func(i)])
    points=np.append(points, [new_row], axis=0)
#------------------------------------------

for x_interp in range (-5, 6):
    y_interp = piecewiselinear_interploation(points, x_interp)
    interpoansw.append(["x ={:8.4f}, interpolated y ={:8.4f}, f(x) ={:8.4f}".format( x_interp, y_interp, func(x_interp))])

for x_interp in range (-5, 6):
    y_interp = lagrange_interpolation(points, x_interp)
    lagrpoansw.append(["x ={:8.4f}, interpolated y ={:8.4f}, f(x) ={:8.4f}".format( x_interp, y_interp, func(x_interp))])

#-----------ANSWERS--------------
for i in eqsppoint:
    print("equally-spaced 15 points in [−5, 5]: ", i)         '''Yeah, its bullshit, i know'''
                                                            '''I have not more time''' 
for i in interpoansw: 
    print("Answer #1: ", i)
for i in lagrpoansw:
    print("Answer#2:" , i)
