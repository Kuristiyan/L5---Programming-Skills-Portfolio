from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

quiz = Tk() # Creates the window
quiz.title("Maths Quiz") # Window title
quiz.geometry("400x400") # Window size
quiz.resizable(False, False) # Fixed window size
quiz.configure(bg = "#0A192F") # Window background color


def displayMenu(): # Displays the menu of the quiz
    clear() # Clears the window
    quizl = Label(quiz, text = "+ - ARITHMETIC QUIZ - +", font = ("Arial", 20), fg = "#C5C7BC", bg = "#0A192F") # Quiz title
    quizl.pack(pady = 20)
    difl = Label(quiz, text = "QUIZ DIFFICULTY LEVEL", font = ("Arial", 15), fg = "#C5C7BC", bg = "#0A192F") # Difficulty level options sign
    difl.pack(pady = 15)
    easb = Button(quiz, text = "1. Easy", font = ("Arial", 13), fg = "#555346", command = easyq) # Easy option, activates easy quiz
    easb.pack(pady = 13)
    modb = Button(quiz, text = "2. Moderate", font = ("Arial", 13), fg = "#555346", command = modq) # Moderate option, activates moderate quiz
    modb.pack(pady = 13)
    advb = Button(quiz, text = "3. Advanced", font = ("Arial", 13), fg = "#555346", command = advq) # Advanced option, activates advanced quiz
    advb.pack(pady = 13)


def easyq(): # Calling the easy level
    quizStart(1)


def modq(): # Calling the moderate level
    quizStart(2)


def advq(): # Calling the advanced level
    quizStart(3)

    
def randomInt(diff): # Generates random number based on the selected difficulty
    if diff == 1: # Selected difficulty
        return random.randint(1, 9) # Returns a random number between 1-9
    elif diff == 2: # Selected difficulty
        return random.randint(10, 99) # Returns a random number between 10 - 99
    else: # Selected difficulty
        return random.randint(1000, 9999) # Returns a random number between 1000 - 9999


def decideOperation(): 
    return random.choice(['+', '-']) # Randomly chooses an arithmetic operator


def displayProblem(): # Displays quiz question and input fields
    clear() # Clears the window
    upques = Label(quiz, text = f"Question {qnum+1} of 10", font = ("Arial", 20), fg = "#C5C7BC", bg = "#0A192F") # Displays question number
    upques.pack(pady = 40)
    questions = Label(quiz, text = f"{num1} {operator} {num2} =", font = ("Arial", 18), fg = "#C5C7BC", bg = "#0A192F") # Displays arithmetic question
    questions.pack(pady = 15)
    
    global user_answer # Saves user input into a global variable
    user_answer = Entry(quiz, font = ("Arial", 15), fg = "#0A192F", justify = 'center') # Displays a text box for the user to input their answer
    user_answer.pack(pady = 15)

    ansb = Button(quiz, text = "Submit", font = ("Arial", 13), fg = "#555346", command = isCorrect) # Submits user's answer
    ansb.pack(pady = 15)


def isCorrect(): # Checks if the user's answer matches the correct answer
    global score, attempt, qnum # Modifies global variables
    try:
        user = int(user_answer.get()) # Converts user's input to an integer
    except:
        messagebox.showerror("Error", "Invalid Input: Enter a number.") # Activates if user's input is invalid
        return

    correct_ans = num1 + num2 if operator == '+' else num1 - num2 # Calculates  and stores the correct answer

    if user == correct_ans: # If user inputs a correct answer
        if attempt == 1:
            score += 10 # Adds 10 points if first try
        else:
            score += 5 # Adds 5 points if second try
        messagebox.showinfo("Correct", "Correct Answer!")
        nextQ()
    else:
        if attempt == 1:
            attempt = 2 # Gives second chance if user answers incorrectly
            messagebox.showwarning("Incorrect", "Wrong answer! Try Again!")
            displayProblem()
        else: # Activates when two consecutive incorrect answers
            messagebox.showwarning("Incorrect", f"Consecutive Incorrect Answer! Answer {correct_ans}")
            nextQ()


def nextQ(): # Moves to the next question
    global qnum, num1, num2, operator, attempt # Modifies global variables
    qnum += 1 # Increments the question number
    if qnum == 10: # Activates if there are no more questions
        displayResults()
    else: # If quis is not yet finished, generates new question
        num1 = randomInt(diff)
        num2 = randomInt(diff)
        operator = decideOperation()
        attempt = 1
        displayProblem()


def displayResults(): # Displays the final quiz results
    clear() # Clears the window
    finishl = Label(quiz, text = "QUIZ COMPLETED!", font = ("Arial", 20), fg = "#C5C7BC", bg = "#0A192F")
    finishl.pack(pady = 20)
    result = Label(quiz, text = f"Score: {score}/100", font = ("Arial", 15), fg = "#C5C7BC", bg = "#0A192F") # Displays user's final score
    result.pack(pady = 15)

    # Assigns marks by user's scores
    if score >= 90:  
        mark = "A+!"
    elif score >= 80:
        mark = "A!"
    elif score >= 70:
        mark = "B!"
    elif score >= 60:
        mark = "C"
    elif score >= 50:
        mark = "D"
    else:
        mark = "F"

    markl = Label(quiz, text = f"Grade: {mark}", font = ("Arial", 20), fg = "#C5C7BC", bg = "#0A192F") # Displays user's marks
    markl.pack(pady = 15)
    restartb = Button(quiz, text = "Quiz Again?", font = ("Arial", 13), fg = "#555346", command = displayMenu) # Restart button
    restartb.pack(pady = 20)
    exitb = Button(quiz, text = "Exit Quiz", font = ("Arial", 13), fg = "#555346", command = quiz.quit) # Exit button
    exitb.pack(pady = 15)


def quizStart(lvl): # Initializes the quiz
    global diff, score, qnum, attempt, num1, num2, operator # Sets up global variables
    diff = lvl # Sets difficulty level
    score = 0 # Sets user's score
    qnum = 0 # Sets question number
    attempt = 1 # Sets user's chances
    num1 = randomInt(diff) # Generates the first question
    num2 = randomInt(diff) # Generates the first question
    operator = decideOperation() # Generates the first question
    displayProblem() # Displays first question

def clear():
    for widgets in quiz.winfo_children(): # Loops through all widgets
        widgets.destroy() # Clears all widfet and prepares the window for the next screen


displayMenu() # Runs the first screen
quiz.mainloop() # Runs the main window