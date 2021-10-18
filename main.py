import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Guessing Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50', prompt="What's another state?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == answer_state]
        t.goto(int(data_state.x), int(data_state.y))
        t.write(answer_state)
    elif answer_state == "Exit":
        break

states_to_guess = [state for state in all_states if state not in guessed_states]
# for state in all_states:
#     if state not in guessed_states:
#         states_to_guess.append(state)

df = pandas.DataFrame(states_to_guess)
df.to_csv("states_to_guess.csv")

screen.exitonclick()
