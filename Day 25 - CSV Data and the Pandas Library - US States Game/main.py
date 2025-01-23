import turtle
import pandas

def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape("blank_states_img.gif")
    turtle.shape("blank_states_img.gif")
    states_dataframe = pandas.read_csv("50_states.csv")
    states_list =  states_dataframe["state"].tolist()
    correct_answers = 0
    correct_guesses_list = []

    while correct_answers < 50:
        answer_state= str(screen.textinput(title=f"{correct_answers} States Correct", prompt="What's another state's name'")).title()
        if answer_state.lower() == "exit":
            states_to_learn = []
            for state in states_list:
                if state not in correct_guesses_list:
                    states_to_learn.append(state)
            new_data = pandas.DataFrame(states_to_learn)
            new_data.to_csv("states_to_learn.csv")
            print(new_data)

            break
        if answer_state in states_list:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states_dataframe[states_dataframe["state"] == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)
            correct_answers += 1
            correct_guesses_list.append(answer_state)


    turtle.mainloop()


main()