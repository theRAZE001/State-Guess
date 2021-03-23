import turtle
import pandas


class UserGuess:
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.tolist()
    guessed_state = []

    def __init__(self):
        self.answer = None

    def user_input(self):
        screen = turtle.Screen()
        while len(self.guessed_state)<51:
            self.answer = screen.textinput("Guess the states", f"{len(self.guessed_state)}/50").title()

            if self.answer == "Exit":
                missing_states =[]
                for states in self.state_list:
                    if states not in self.guessed_state:
                        missing_states.append(states)
                    missed_data = pandas.DataFrame(missing_states)
                    missed_data.to_csv("missing_states.csv")
                break

            if self.answer in self.state_list and self.answer not in self.guessed_state:
                self.guessed_state.append(self.answer)
                self.move_state()

    def move_state(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_name = self.data[self.data.state == self.answer]
        t.goto(int(state_name.x), int(state_name.y))
        t.write(self.answer)



