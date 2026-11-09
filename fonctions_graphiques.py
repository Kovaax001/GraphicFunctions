import tkinter as tk
import convert_equations
import math

print("Fonction :")
f = convert_equations.create_function(input())   
fenetre = tk.Tk()
fenetre.title("Ma fonction")
canvas = tk.Canvas(fenetre, width=600, height=400, bg="white")
canvas.pack()
def vers_pixel(x, y):
    px = (x - xmin) / (xmax - xmin) * LARGEUR
    py = HAUTEUR - (y - ymin) / (ymax - ymin) * HAUTEUR
    return px,py
LARGEUR = 600
HAUTEUR = 400
MARGE = 20
xmin, xmax = -10, 10
ymin, ymax = -1.5, 1.5
milieu_x, milieu_y = vers_pixel(0, 0)
milieu_x = max(MARGE, min(LARGEUR - MARGE, milieu_x))
milieu_y = max(MARGE, min(HAUTEUR - MARGE, milieu_y)) 
canvas.create_line(0,milieu_y, LARGEUR,milieu_y )
canvas.create_line(milieu_x, 0, milieu_x, HAUTEUR)
abscisse = xmin
a = 0
ordonne = ymin
b = HAUTEUR
for v in range(math.ceil(xmin),math.floor(xmax)+1):
    a,b = vers_pixel(v,0)
    canvas.create_line(a, milieu_y - 3, a, milieu_y + 3)
    if v != 0:
        canvas.create_text(a, milieu_y + 12, text=v)
for v in range(math.ceil(ymin),math.floor(ymax)+1):
    c,d = vers_pixel(0,v)
    canvas.create_line(milieu_x - 3, d, milieu_x + 3, d)
    if v != 0:
        canvas.create_text(milieu_x - 12, d, text=v)
        
    
points = []
for i in range(LARGEUR + 1):
    x = xmin + i * (xmax - xmin) / LARGEUR
    y = f(x)
    px, py = vers_pixel(x, y)
    points.append(px)
    points.append(py)
canvas.create_line(points)

fenetre.mainloop()

