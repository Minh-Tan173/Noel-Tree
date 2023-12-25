import turtle as t
from turtle import *
import random as r
import time
from PIL import Image, ImageTk, ImageFilter

# Function to blur the image
def blur_image(image_path, blur_radius):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

t.title("Mừng noel")
n = 100.0
speed("fastest")
# Background
background_image_path =r"C:\Users\admin\OneDrive\Máy tính\final exam\asset\Screenshot 2023-12-24 175516.jpg"
blurred_background = blur_image(background_image_path, blur_radius=5)  # Adjust blur_radius as needed
blurred_background_path = "blurred_background.gif"
blurred_background.save(blurred_background_path)
t.bgpic(blurred_background_path)

left(90)
t.color("dark red", "red")

forward(2.5 * n)
color("red", "yellow")
begin_fill()
left(126)
for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)


def drawlight():
    if r.randint(0, 20) == 0:
        color("red")
        begin_fill()  # Bắt đầu đổ màu
        circle(6)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 2:
        color('yellow')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 4:
        color('yellow')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 1:
        color('green')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    elif r.randint(0, 20) == 3:
        color('green')
        begin_fill()  # Bắt đầu đổ màu
        circle(3)
        end_fill()  # Kết thúc đổ màu
    else:
        color('dark green')


color("dark green")
backward(n * 4.8)


def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    begin_fill()  # Bắt đầu đổ màu
    circle(3)
    end_fill()  # Kết thúc đổ màu
    up()
    backward(a)
    right(90)
    backward(b)

t.pencolor("dark red")

def drawsnow():
    t.ht()
    t.pensize(2)
    for i in range(200):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-500, 500))
        t.sety(r.randint(-500, 500))
        t.pd()
        dens = 6
        snowsize = r.randint(1, 10)
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))


# Loop for changing text color continuously
while True:
    custom_x = 30
    custom_y = -350

    text_color = (r.random(), r.random(), r.random())  # Random RGB values
    t.penup()
    t.goto(custom_x, custom_y)  # Set custom position
    t.pendown()
    
    t.color(text_color)
    t.write("Merry Christmas to my cherished friends\n         May your days be filled with joy", align="center", font=("Agbalumo", 22))
    time.sleep(1)  # Delay for 1 second before changing color again

    
drawsnow()

os.remove(blurred_background_path)

t.done()

