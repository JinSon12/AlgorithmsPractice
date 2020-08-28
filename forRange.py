import turtle as t

t.shape("turtle")

angle = 89
t.bgcolor("black")
t.color("green")
t.speed(3)
for x in range(200):
    t.forward(x)
    t.left(angle)
t.mainloop()
