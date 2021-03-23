import turtle
from guessBox import UserGuess

screen = turtle.Screen()
screen.title("US State Challenge")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
guess = UserGuess()


#def get_mouse_click(x, y):
#    print(x,y)

#turtle.onscreenclick(get_mouse_click)
#turtle.mainloop()

guess.user_input()
