#Kayla Jackson
#07/03/24
#P4LAB1
# Create squar and triangle using turtle graphics. 



import turtle


screen = turtle.Screen()
screen.title("Square and Triangle Drawing")


artist = turtle.Turtle()


def draw_square():
    for _ in range(4):
        artist.forward(100) 
        artist.right(90)   

def draw_triangle():
    for _ in range(3):
        artist.forward(100)  
        artist.right(120)    


draw_square()

artist.penup()
artist.goto(-50, -50)  
artist.pendown()


draw_triangle()


artist.hideturtle()
turtle.done()
