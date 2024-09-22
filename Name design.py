#  Importing turtle module
import turtle as t

#  Setting place of pen
t.bgcolor('navy')
t.pencolor('aqua')
t.penup()
t.bk(240)
t.right(90)
t.fd(100)
t.left(90)
t.pendown()
t.pensize(10)
t.right(45)
t.fd(200)

#  Making octagon and filling color
t.fillcolor('yellow')
t.begin_fill()
for i in range(7):
    t.left(45)
    t.fd(200)
t.end_fill()
t.penup()
t.right(180)
t.fd(200)
t.right(45)
t.fd(200)
t.right(45)
t.fd(308)
t.right(90)
t.fd(239)
t.pendown()


#  Making circle and filling color
t.fillcolor("pink")
t.begin_fill()
t.pencolor('green')
t.circle(-210)
t.end_fill()
t.penup()
t.right(90)
t.fd(205)
t.left(90)
t.fd(290)

#  Writing "Alphabet" 
t.pencolor('blue')
t.pensize(12)
t.pendown()
t.write('Z',align='center',font=('Courier','390', 'normal'))


#  Making crown 
t.penup()
t.left(180)
t.fd(570)
t.left(90)
t.fd(103)
t.right(90)
t.pendown()
t.pencolor('gold')
t.fillcolor('gold')
t.begin_fill()
t.fd(100)
t.right(135)
t.fd(80)
t.left(100)
t.fd(80)
t.right(110)
t.fd(80)
t.left(100)
t.fd(80)
t.right(135)
t.fd(100)
t.right(90)
t.fd(200)
t.end_fill()

t.done()

