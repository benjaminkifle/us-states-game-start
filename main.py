import turtle
import pandas

# Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Variables
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
missing_states = []

# Running the game
while len(guessed_states) < 50:

    # Asking for an answer and saving it in a variable
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Exits the game loop and creates a new CSV file with all the missing states
    if answer_state == "Exit":
        for states in state_list:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Checking if user guess is correct and writing it at the appropriate location on the map
    if answer_state in state_list and answer_state not in guessed_states:
        state_info = data[data.state == answer_state]
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(int(state_info.x), int(state_info.y))
        new_state.write(f"{answer_state}", font=("Courier", 12, "normal"))
        guessed_states.append(answer_state)


screen.exitonclick()
