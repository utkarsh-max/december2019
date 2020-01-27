from tkinter import *
from tkinter import messagebox,ttk,filedialog
from tkinter import ttk
import pymysql
from  datetime import datetime
taz=Tk()

############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback
############# def logout ########################
#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
############ mainheading creation ###########
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 40, "bold"), padx=0, pady=0)
    label.grid(row=0, columnspan=4)
##############################################
############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor()

############ Welcome window ############
def welcomewindow():
    remove_all_widgets()
    mainheading()
    loginButton = Button(taz, text="logout", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=6, column=1, columnspan=2)

############### admin Login ###################
def adminlogin():
    username = usernameVar.get()
    password = passwordVar.get()
    if(username=="" or password==""):
        messagebox.showerror("Data Filling Error","Please Fill user Name and Password both")
    else:
        dbconfig()
        que = "select * from user_info where userid=%s and password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        conn.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            usernameVar.set("")
            passwordVar.set("")

##########################################
############### login window ####################
usernameVar = StringVar()
passwordVar = StringVar()

def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)
    usernameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)


################################################
screen_width=taz.winfo_screenwidth()
#print(screen_width)
screen_height=taz.winfo_screenheight()
#print(screen_height)
taz.title("Hotel WAhTaz Managment System")
mainheading()
loginwindow()

#taz.geometry("900x600+120+50")
taz.geometry("%dx%d+0+0"%(screen_width,screen_height))
mainloop()