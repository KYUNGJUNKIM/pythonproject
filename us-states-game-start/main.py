import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guess = []

score = 0
while len(guess) < 50:
    answer = screen.textinput(title=f"{score}/50 states correct", prompt="Enter any States in U.S.").title()
    guess.append(answer)
    if answer == "Exit":
        missed_states = []
        for state in states:
            if state not in guess:
                missed_states.append(state)
        learn = pandas.DataFrame({"state": missed_states})
        learn.to_csv("states_to_learn.csv")
        break

    ### Same Code with def title()
    # if " " in answer:
    #     head = answer.split(" ")[0]
    #     tail = answer.split(" ")[1]
    #     answer = head[0].upper() + head[1:] + " " + tail[0].upper() + tail[1:]
    # else:
    #     answer = answer[0].upper() + answer[1:]

    location = [(row.x, row.y) for index, row in data.iterrows() if answer == row.state]

    if answer in states:
        score += 1
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(location[0][0], location[0][1])
        state.write(answer, align="center")









