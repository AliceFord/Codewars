from math import *

#
# def circleIntersection(a, b, r):
# 	d = sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
# 	if d < 2 * r:
# 		A = r*r
# 		x = d/2
# 		z = x**2
# 		y = sqrt(A - z)
#
# 		return int(2 * A * asin(y / r) - y * (x + sqrt(x)))
#
# 	return 0


def circleIntersection(A, B, r):
	d = sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)

	if d < 2 * r:
		a = r * r
		b = r * r
		x = d / 2
		z = x * x
		y = sqrt(a - z)

		if d <= abs(r - r):
			return int(pi * min(a, b))
		return int(a * asin(y / r) + b * asin(y / r) - y * (x + sqrt(z + b - a)))


print(circleIntersection([0, 0],[7, 0],5)==14)
print(circleIntersection([0, 0],[0, 10],10)==122)
print(circleIntersection([5, 6],[5, 6],3)==28)
print(circleIntersection([-5, 0],[5, 0],3)==0)
print(circleIntersection([10, 20],[-5, -15],20)==15)
print(circleIntersection([-7, 13],[-25, -5],17)==132)
print(circleIntersection([-20, -4],[-40, 29],7)==0)
print(circleIntersection([38, -18],[46, -29],10)==64)
print(circleIntersection([-29, 33],[-8, 13],15)==5)
print(circleIntersection([-12, 20],[43, -49],23)==0)
