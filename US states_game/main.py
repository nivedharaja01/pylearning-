import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/nivedhagowtham/Desktop/BA-docs /python_files/day-25-us-states-game-start/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/nivedhagowtham/Desktop/BA-docs /python_files/day-25-us-states-game-start/50_states.csv")

all_states = data.state.to_list()
guessed_states = []

#def get_mouse_click_coor(x,y):
    #print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

while len(guessed_states)<50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                prompt= "Whats another state's name?")
    if answer_state is None:
        break 
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("/Users/nivedhagowtham/Desktop/BA-docs /python_files/day-25-us-states-game-start/states_to_learn.csv")

        break

    answer_state = answer_state.title()

    if answer_state in all_states:
       guessed_states.append(answer_state) 
       t = turtle.Turtle()
       t.hideturtle()
       t.penup()
       state_data = data[data.state == answer_state]
       t.goto(state_data.x.item(),state_data.y.item())
       t.write(state_data.state.item())



