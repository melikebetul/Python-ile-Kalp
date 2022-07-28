# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:20:05 2022

@author: Melike Betül Çakan

"""
import turtle
pen = turtle.Turtle()
#pen.ht()

def curve(t): 
    for i in range(200):
        pen.right(1)
        pen.forward(1)

        t+=1

    return t

def straightLine(times:int, t):
    for i in range(times):
        pen.right(1)
        pen.left(1)
        pen.forward(1)

        t+=1
        
    return t

def heart():    
    pen.fillcolor('pink')
    pen.pencolor('pink')
  
    pen.begin_fill()
  
    pen.left(140)
    t = straightLine(113, 0)
  
    t = curve(t)
    pen.left(120)
    
    t = curve(t)
    t = straightLine(112, t)
    
    pen.end_fill()
    
    
def txt():
  
    pen.up()

    pen.setpos(-68, 95)
  
    pen.down()
  
    pen.color('blue')
  
    pen.write("University4Society", font=(
      "Verdana", 12, "bold"))
heart()
txt()
pen.ht()
