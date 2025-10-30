from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

sm = Tk() # Creates the window
sm.title("Student Manager") # Window title
sm.geometry("1075x720") # Window size
sm.configure(bg = "#e6ecf0") # Window background color
 

def open_list():
    student_list = [] # Empty list to store students' data
    try:
        with open("studentMarks.txt", "r") as f: # Open .txt file for reading
            lines = [line.strip() for line in f if line.strip()] # Removes any whitespaces from the line
            for line in lines[1:]:
                parts = line.split(",") # Separate each line into small values by commas
                code = parts[0]
                name = parts[1]
                c1 = int(parts[2])
                c2 = int(parts[3])
                c3 = int(parts[4])
                exam = int(parts[5])
                student_list.append([code, name, c1, c2, c3, exam])
    except FileNotFoundError: # This activates when file is not found
        messagebox.showerror("Error", "studentMarks.txt not found.") # Messagebox for the error
    return student_list


def save_new_students():
    with open("studentMarks.txt", "w") as f: # Overwrites old file
        f.write(str(len(students)) + "\n")
        for s in students: # Loop to write all values as a comma-separated line
            line = f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]},{s[5]}\n"
            f.write(line) 


def total_coursework_marks(student):
    return student[2] + student[3] + student[4] # Add all the coursework marks


def total_marks(student):
    cw = total_coursework_marks(student) # Store coursework marks
    exam = student[5] # Store exam marks
    return cw + exam # Add coursework marks + exam marks 


def marks_percentage(student):
    return round(total_marks(student) / 160 * 100, 2) # Covert total marks to a percentage and rounds it to 2 decimal places


def students_grades(student):
    p = marks_percentage(student) # Assigns grades by percentage ranges
    if p >= 70:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "F"


def output_txtarea(text):
    txtarea.config(state = "normal") # Makes the text area / text box editable
    txtarea.delete("1.0", "end") # Clears the old content
    txtarea.insert("end", text) # Inserts new text
    txtarea.config(state = "disabled") # Makes the text area / text box  un-editable


def student_display(student): # String formatting with all the students' details
    text = ""
    text += f"Name: {student[1]}\n"
    text += f"Student Number: {student[0]}\n"
    text += f"Total Coursework: {total_coursework_marks(student)}\n"
    text += f"Exam Mark: {student[5]}\n"
    text += f"Overall %: {marks_percentage(student)}\n"
    text += f"Grade: {students_grades(student)}\n"
    return text


def view_all():
    if len(students) == 0: # Checks if list is empty
        output_txtarea("No Student Records found.") # Output if the list is empty
        return

    text = ""
    total_percent = 0

    for s in students: # Loops through all student listed, formatting their records
        text += student_display(s)
        text += "\n" + "-" * 100 + "\n" + "\n"
        total_percent += marks_percentage(s)

    avg = total_percent / len(students) # Gets the students' percentages for average
    text += f"\nNumber of students: {len(students)}\n" 
    text += f"Average Percentage: {avg:.2f}%" # Calculates class average
    output_txtarea(text) # Prints the output on the text area


def view_highest():
    if len(students) == 0: # Checks if list is empty
        output_txtarea("No Student Records found.") # Output if the list is empty
        return


    best = students[0] # After comparing, assume the first student is the highest
    best_score = total_marks(best)

    for s in students: # Loops through all students to compare their total scores
        if total_marks(s) > best_score:
            best = s
            best_score =total_marks(s)

    text = "Highest Scoring Student:\n\n" + student_display(best)
    output_txtarea(text) # Prints the highest student's record


def view_lowest():
    if len(students) == 0: # Checks if list is empty
        output_txtarea("No Student Records found.") # Outputif the list is empty
        return

    worst = students[0] # After comparing, assume the first student is the lowest
    worst_score = total_marks(worst)

    for s in students: # Loops through all students to compare their total scores
        if total_marks(s) < worst_score:
            worst = s
            worst_score = total_marks(worst)

    text = "Lowest Scoring Student:\n\n" + student_display(worst)
    output_txtarea(text) # Prints the lowest student's record


def view_one():
    name = studentdd.get() # Gets the selected name from the dropdown widget
    if name == "": # Checks if nothing is selected
        messagebox.showinfo("Info", "Please select a valid student.") # Messagebox for the error
        return

    for s in students: # Loops through the list until the selected student is found
        if s[1] == name:
            text = student_display(s)
            output_txtarea(text) # Displays the selected and matched student
            return

    messagebox.showerror("Not found!", "Student not found!") # Displays error if no match is found


def sorting_options(): # Displaying the sorting option to the user
    sort_group.pack(pady=10)


def sort():
    order = sorting_order.get() # Checks if a sort order is selected
    if order not in ["Ascending", "Descending"]: # Activates when no order is selected
        messagebox.showerror("Error!", "Please choose a sort order!") # Messagebox for the error
        return

    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            score1 = total_marks(students[j])
            score2 = total_marks(students[j + 1])
            if order == "Ascending": # If ascending, smaller scores go first
                if score1 > score2:
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp
            else: # If descending, higher scores go first
                if score1 < score2:
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp

    save_new_students() # Saves sorted order
    sort_group.pack_forget() # Hides the sorting frame
    view_all() # Displays the updated list


def add_student():
    code = simple_input("Enter Student Number (1000-9999):") # Displays a window a user can use to enter info
    if not code:
        return

    name = simple_input("Enter Student Name:")
    if not name:
        return

    try: # Converts all user input into integers
        c1 = int(simple_input("Enter Coursework 1 Mark (out of 20):"))
        c2 = int(simple_input("Enter coursework 2 Mark (out of 20):"))
        c3 = int(simple_input("Enter coursework 3 Mark (out of 20):"))
        exam = int(simple_input("Enter Examination Mark (out of 100):"))
    except: # If user input is unconvertable
        messagebox.showerror("Error!", "Invalid mark entered!") # Messagebox for the error
        return

    new_student = [code, name, c1, c2, c3, exam] # Stores the new student's info
    students.append(new_student) # Adds the student in the list
    save_new_students() # Saves the list 
    update_combobox() # Updates the dropdown widget
    messagebox.showinfo("Success!", "Student records added successfully!") # Messagebox for the successful procedure
    view_all()


def delete_student():
    name = simple_input("Enter Student Name or Number to Delete:") # Displays a window a user can use to select a listed student
    if not name:
        return

    found = False
    for s in students: 
        if s[1].lower() == name.lower() or s[0] == name: # Activates when selected student is found found
            students.remove(s) # Removes the record
            save_new_students() # Saves the file
            update_combobox() # Updates the dropdown widget
            messagebox.showinfo("Deleted!", "Student records deleted!") # Messagebox for the successful procedure
            view_all()
            found = True
            break

    if not found: # Activates if not found, display an error box
        messagebox.showerror("Not found!", "Student records not found!") # Messagebox for the error


def update_student():
    name = simple_input("Enter the Student Name or Number to Update:") # Displays a window a user can use to select a listed student
    if not name:
        return

    for s in students:
        if s[1].lower() == name.lower() or s[0] == name: # If found, asks what field to update
            field = simple_input("Which field? (Name, C1, C2, C3, Exam):")
            if not field:
                return

            if field.lower() == "name": # Updates name
                newval = simple_input("Enter new name:")
                s[1] = newval

            elif field.lower() in ["c1", "c2", "c3", "exam"]: # Updates intger marks
                try:
                    newval = int(simple_input("Enter new mark:"))
                    if field == "c1":
                        s[2] = newval
                    elif field == "c2":
                        s[3] = newval
                    elif field == "c3":
                        s[4] = newval
                    elif field == "exam":
                        s[5] = newval
                except:
                    messagebox.showerror("Error!", "Invalid mark!") # Messagebox for the error
                    return
            else:
                messagebox.showerror("Error!", "Invalid field!") # Messagebox for the error
                return

            save_new_students() # Rewrites and saves the updated field
            update_combobox() # Updates the dropdown widget
            messagebox.showinfo("Updated!", "Record updated!") # Messagebox for the successful procedure
            view_all()
            return

    messagebox.showerror("Not found!", "Student not found!") # Messagebox for the error


def quit():
    sm.destroy() # Closes the program


def simple_input(prompt):
    pu_window = tk.Toplevel(sm) # Creates a small pop-up window
    pu_window.title("Input")
    Label(pu_window, text = prompt).pack(pady = 10)
    entry = Entry(pu_window, width = 30)
    entry.pack(pady = 10)

    val = [] # Variable for storing the user input

    def confirm(): # Stores the user input
        value = entry.get()
        val.append(value)
        pu_window.destroy()

    Button(pu_window, text = "OK", command = confirm).pack(pady = 10)
    pu_window.wait_window()
    if len(val) > 0:
        return val[0]
    else:
        return None


def update_combobox(): # Updates the dropdown widget anytime the file changes
    names = []
    for s in students:
        names.append(s[1])
    studentdd["values"] = names


students = open_list() # Loads the file


menu_bar = Menu(sm) # Creates the menu bar
sm.config(menu = menu_bar) 
menu_options = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Extended Menu", menu = menu_options) # Menu bar title
menu_options.add_command(label = "Add New Student", command = add_student) # Add option
menu_options.add_command(label = "Delete Student", command = delete_student) # Delete option
menu_options.add_command(label = "Update Student", command = update_student) # Update option
menu_options.add_separator() # Line in-between
menu_options.add_command(label = "Sort Records", command = sorting_options) # Sort option
menu_options.add_separator() # Line in-between
menu_options.add_command(label = "Exit Program", command = quit) # Exit option


titlel = Label(sm, text = "Student Manager", font = ("Times New Roman", 25, "bold"), bg = "#e6ecf0") # Title Label
titlel.pack(pady=10)


buttons_group = Frame(sm, bg = "#e6ecf0") # Groups up the buttons in the same row
buttons_group.pack(pady = 5)
viewallb = Button(buttons_group, text = "View All Students", width = 20, height = 2, bg = "#28527a", fg = "white", font = ("Times New Roman", 12, "bold"), command = view_all) # Big button for a specific viewing option
viewallb.grid(row = 0, column = 0, padx = 10, pady = 5)
viewhb = Button(buttons_group, text = "Show Highest Scorer", width = 20, height = 2, bg = "#28527a", fg = "white", font = ("Times New Roman", 12, "bold"), command = view_highest) # Big button for a specific viewing option
viewhb.grid(row = 0, column = 1, padx = 10, pady = 5)
viewlb = Button(buttons_group, text = "Show Lowest Scorer", width=20, height=2, bg="#28527a", fg="white", font=("Times New Roman", 12, "bold"), command=view_lowest) # Big button for a specific viewing option
viewlb.grid(row = 0, column = 2, padx = 10, pady = 5)


selection_group = Frame(sm, bg = "#e6ecf0") # Groups up the label, dropdown, and button widget that are in the same row
selection_group.pack(pady = 10)
selectl = Label(selection_group, text = "Select Student:", bg = "#e6ecf0", font = ("Times New Roman", 12)) # Dropdown sign
selectl.grid(row = 0, column = 0, padx = 5)
studentdd = ttk.Combobox(selection_group, width = 30, state = "readonly") # Dropdown list for selecting a student
studentdd.grid(row = 0, column = 1, padx = 5)
viewoneb = Button(selection_group, text = "View Record", fg = "white", font = ("Times New Roman", 10, "bold"), command = view_one, bg = "#28527a", width = 15) # Views the selected student
viewoneb.grid(row = 0, column = 2, padx = 5)


update_combobox() # Updates the dropdown list


sort_group = Frame(sm, bg = "#d9e2ec", padx = 10, pady = 10, relief = "ridge", bd = 2) # Groups all the widgets that are involed in sorting function in a hidden section
sortl = Label(sort_group, text = "Sort Students by Total Score", bg = "#d9e2ec", font = ("Times New Roman", 12, "bold")) # Sorting sign
sortl.pack()
sorting_order = StringVar()
ascrb = tk.Radiobutton(sort_group, text = "Lowest to Highest", variable=sorting_order, value = "Ascending", bg="#d9e2ec") # Radiobutton for selecting a sorting type
ascrb.pack(anchor="w")
descrb = tk.Radiobutton(sort_group, text = "Highest to Lowest", variable=sorting_order, value = "Descending", bg="#d9e2ec") # Radiobutton for selecting a sorting type
descrb.pack(anchor="w")
sortb = Button(sort_group, text = "Sort", command = sort, bg="#28527a", fg = "white") # Activates sort
sortb.pack(pady = 5)


txtarea_group = tk.Frame(sm, bg = "#d9e2ec") # Groups all the widgets involved in the text area / text box
txtarea_group.pack(fill = "both", expand = True, padx = 20, pady = 10) 
scrollbar = Scrollbar(txtarea_group) # Creates a scrollbar
scrollbar.pack(side = "right", fill = "y") # Positions the scrollbar
txtarea = Text(txtarea_group, wrap="word", height=18, width=90, font = ("Courier", 12), yscrollcommand=scrollbar.set) # Large text area that displays all results
txtarea.pack(side="left", fill="both", expand=True, pady = 15)
scrollbar.config(command=txtarea.yview)
txtarea.config(state = "disabled", bg = "#f8f9fa")


sm.mainloop() # Runs the main window
