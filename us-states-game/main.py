import turtle
import pandas
# creen setup
correct_guess_list = []
screen = turtle.Screen()
screen.title(" U.S State Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


# import the dataset as a csv

data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()

# getting user guess
while len(correct_guess_list) < 50:
    answer = screen.textinput(title=f'{len(correct_guess_list)}/ 50 Guess the Sate',
                              prompt="what's another state's name").title()

    # detect when user want to exit the game  and return a list of all the messing states
    if answer == 'Exit':
        remaining_state = [
            state for state in data.state if state not in correct_guess_list]
        state_learn = pandas.DataFrame(remaining_state)
        state_learn.to_csv('state_learn.csv')
        break

        # checking the user impurt againt the state list in the dataset

    if answer in state_list:
        correct_guess_list.append(answer)
        state_choice = data[data['state'] == answer]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x = int(state_choice.x)
        y = int(state_choice.y)

        # write the sate on the coresponding state
        state.goto(x, y)
        state.write(state_choice.state.item())
    else:
        # if user input does not match any state return NONE!
        print('None')
