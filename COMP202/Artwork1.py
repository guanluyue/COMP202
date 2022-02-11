#Name: Luyue (Gwen) Guan
#Student ID: 260950108
import turtle
import random
def circles(pensize, num_circles):
    '''
    (int, int) -> void
    
    Draws circles with different diameters
    '''
    for i in range(num_circles):
        c = turtle.Turtle()
        c.hideturtle()
        c.speed('fastest')
        c.pensize(pensize)
        if i == 0:
            c.fillcolor('orange')
            c.begin_fill()
            c.penup()
            c.goto(75, -200)
            c.pendown()
            c.circle(95)
            c.end_fill()
            continue
        elif i == 1:
            c.fillcolor('blue')
            c.begin_fill()
            c.penup()
            c.goto(75, -185)
            c.pendown()
            c.circle(80)
            c.end_fill()
            break
    
def letter_L():
    '''
    () -> void
    
    Draws a orange letter L on top of the circles
    '''
    L = turtle.Turtle()
    L.hideturtle()
    L.fillcolor('orange')
    L.begin_fill()
    L.speed('fastest')
    L.pensize(8)
    L.forward(70)
    L.right(90)
    L.forward(174)
    L.left(90)
    L.forward(95)
    L.right(120)
    L.forward(30)
    L.right(60)
    L.forward(150)
    L.right(120)
    L.forward(30)
    L.left(30)
    L.forward(148)
    L.left(30)
    L.forward(30)
    L.end_fill()
 
#My first name is Gwen (also Luyue)
#The letter 'G' is randomly positioned either to the top or the left of the icon
#and the letter 'L' is included in the icon
def initial():
    '''
    () -> void
    
    Draws the letter G randomly either to the top or the left of the icon
    '''
    g = turtle.Turtle()
    g.hideturtle()
    g.speed('fastest')
    g.pensize(20)
    g.color(input('Please enter a color: '))
    pos = random.randint(1, 2)
    g.penup()
    if pos == 1:
        g.goto(0, 150)
    elif pos == 2:
        g.goto(-150, 0)
    g.pendown()
    g.left(180)
    g.circle(50, 270)
    g.left(90)
    g.forward(50)
 
#This function will create a grey suqare boarder around the icon
def boarder():
    '''
    () -> void
    
    Draws a grey square boarder around the icon
    '''
    b = turtle.Turtle()
    b.pensize(5)
    b.color('grey')
    b.hideturtle()
    b.speed('fastest')
    b.penup()
    b.goto(-30, 5)
    b.pendown()
    for i in range(4):
        b.forward(210)
        b.right(90)
 
#This is the icon of League of Legends
def my_artwork():
    '''
    () -> void
    
    Draws the complete icon of League of Legends with the letter G next to it
    '''
    circles(8, 2)
    letter_L()
    initial()
    boarder()
 