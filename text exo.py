import turtle

# Initialisation
t = turtle.Turtle()
t.speed(2)

# Dessiner un cœur
t.fillcolor('red')
t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Cacher le curseur
t.hideturtle()

# Afficher la fenêtre
turtle.done()
