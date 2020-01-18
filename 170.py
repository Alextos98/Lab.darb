# 170.py
# Aleksejs Lučinskis
# 181RDB146

from math import sin, fabs
from time import sleep

def f(x):
	return sin (x)

# Definējam argumenta x robežas
a = 1.1
b = 3.2

# Aprēķinam funkcijas vērtības dotajos punktos
funa = f(a)
funb = f(b)

# Pārbaudām vai dotajā intervālā ir saknes
if (funa * funb > 0.0):
	# Ziņo uz ekrāna, gaida 1 sekundi un darbu pabeidz
	print("Dotajā intervālā [%s, %s] sakņu nav"%(a,b))
	sleep (1); exit ()
else :
	print("Dotajā intervālā sakne(s) ir!")

# Definējam precizitāti ar kādu meklēsim sakni
deltax = 0.01

# Sašaurinām saknes meklēšanas robežas
while (fabs (b-a) > deltax):
	x = (a+b )/2; funx = f(x)
	if (funa * funx < 0.):
		b = x
	else :
		a = x

print ("Sakne ir: " , x)
