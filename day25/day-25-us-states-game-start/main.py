import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guesser = turtle.Turtle()
guesser.penup()
guesser.color("black")
guesser.hideturtle()

data = pd.read_csv("50_states.csv")
names_of_states = data["state"].to_list()

users_guesses = []
while len(users_guesses) < 50:
    user_answer = turtle.textinput(title=f"{len(users_guesses)}/50 States Correct",
                                   prompt="What's another state's name?").title()
    if user_answer == "Exit":
        states_to_learn = [state for state in names_of_states if state not in users_guesses]
        # for state in names_of_states:
        #     if state not in users_guesses:
        #         states_to_learn.append(state)

        new_data = pd.DataFrame(states_to_learn)
        print(new_data)
        new_data.to_csv("missing_states.csv")
        break
    if user_answer in names_of_states:
        users_guesses.append(user_answer)
        correct_state = data[data["state"] == user_answer]
        x = correct_state.x.item()
        y = correct_state.y.item()
        guesser.goto(x, y)
        guesser.write(arg=user_answer, align="center", font=("Ariel", 8, "normal"))


