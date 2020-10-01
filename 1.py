import turtle as t
import numpy as np

a = 10


def one():
    t.penup()
    t.forward(a)
    t.pendown()
    t.setheading(90)
    t.forward(2 * a)
    t.setheading(180 + 45)
    t.forward(a * np.sqrt(2))
    t.penup()
    t.backward(a * np.sqrt(2))
    t.setheading(90)
    t.backward(2 * a)
    t.setheading(0)
    t.forward(a)


def two():
    t.pendown()
    t.setheading(0)
    t.forward(a)
    t.backward(a)
    t.setheading(45)
    t.forward(a * np.sqrt(2))
    t.setheading(90)
    t.forward(a)
    t.setheading(180)
    t.forward(a)
    t.penup()
    t.backward(a)
    t.setheading(-90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)


def three():
    t.pendown()
    for i in range(2):
        t.setheading(45)
        t.forward(a * np.sqrt(2))
        t.setheading(180)
        t.forward(a)
    t.penup()
    t.backward(a)
    t.setheading(-90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)


def four():
    t.forward(a)
    t.setheading(90)
    t.pendown()
    t.forward(a)
    t.setheading(180)
    t.forward(a)
    t.setheading(90)
    t.forward(a)
    t.setheading(0)
    t.penup()
    t.forward(a)
    t.pendown()
    t.setheading(-90)
    t.forward(2 * a)
    t.penup()
    t.setheading(0)
    t.forward(a)


def five():
    t.pendown()
    t.forward(a)
    t.setheading(90)
    t.forward(a)
    t.setheading(180)
    t.forward(a)
    t.setheading(90)
    t.forward(a)
    t.setheading(0)
    t.forward(a)
    t.penup()
    t.setheading(-90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)


def six():
    t.pendown()
    t.forward(a)
    t.setheading(90)
    t.forward(a)
    t.setheading(180)
    t.forward(a)
    t.setheading(-90)
    t.forward(a)
    t.backward(2 * a)
    t.setheading(0)
    t.forward(a)
    t.penup()
    t.setheading(-90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)


def seven():
    t.pendown()
    t.setheading(90)
    t.forward(a)
    t.setheading(45)
    t.forward(a * np.sqrt(2))
    t.setheading(180)
    t.forward(a)
    t.penup()
    t.backward(a)
    t.setheading(-90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)


def eight():
    t.pendown()
    t.forward(a)
    t.backward(a)
    t.setheading(90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)
    t.setheading(-90)
    t.forward(a)
    t.setheading(180)
    t.forward(a)
    t.backward(a)
    t.setheading(-90)
    t.forward(a)
    t.penup()
    t.setheading(0)
    t.forward(a)


def nine():
    t.pendown()
    t.forward(a)
    t.setheading(90)
    t.forward(2 * a)
    t.setheading(180)
    t.forward(a)
    t.setheading(-90)
    t.forward(a)
    t.setheading(0)
    t.forward(a)
    t.setheading(-90)
    t.forward(a)
    t.penup()
    t.setheading(0)
    t.forward(a)


def zero():
    t.pendown()
    t.forward(a)
    t.backward(a)
    t.setheading(90)
    t.forward(2 * a)
    t.setheading(0)
    t.forward(a)
    t.setheading(-90)
    t.forward(2 * a)
    t.penup()
    t.setheading(0)
    t.forward(a)


def num(x):
    if x == "0":
        zero()
    elif x == "1":
        one()
    elif x == "2":
        two()
    elif x == "3":
        three()
    elif x == "4":
        four()
    elif x == "5":
        five()
    elif x == "6":
        six()
    elif x == "7":
        seven()
    elif x == "8":
        eight()
    elif x == "9":
        nine()


inp = open('index.txt', 'r')
index = inp.readline()
for i in range(len(index)):
    num(index[i])
inp.close()
