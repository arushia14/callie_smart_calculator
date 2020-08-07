from Tkinter import *

# Math operations

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def exp(a,b):
    return a ** b

def lcm(x,y):
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm

def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  

# Getting the numeric values from the input field   

def getValues(text):
    li = []
    for t in text.split(' '):
        try:
            li.append(float(t))
        except ValueError:
            pass
    return li

# Check for the operators in the text to implement the calculation

def calculate():
    text = textfield.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = getValues(text)
                r = operations[word.upper()](l[0] , l[1])
                answer.delete(0, END)
                answer.insert(END, r)
            except:
                answer.delete(0, END)
                answer.insert(END, "Oops, please try again!")
            finally:
                break
        elif word.upper() not in operations.keys():
            answer.delete(0, END)
            answer.insert(END, "Please select a valid operation!")


operations = {
    "ADD" : add, "ADDITION": add, "SUM": add, "PLUS": add,
    "SUB" : sub, "SUBTRACT": sub, "DIFFERENCE": sub, "MINUS": sub,
    "MULTIPLY": mul, "MUL": mul, "PRODUCT": mul, "INTO": mul, "MULTIPLICATION": mul,
    "DIVIDE": div, "QUOTIENT": div, "DIV": div, 
    "LCM": lcm, "HCF": hcf, "REMAINDER": mod, "MOD": mod, "MODULUS": mod,
    "EXP": exp, "EXPONENT": exp, "POWER": exp
}


# Frontend layout using Tkinter

win = Tk()
win.geometry('700x400')
win.title("Callie, the Smart Calculator")
win.configure(bg = 'salmon')

label1 = Label(win, text = 'Hi, I am CALLIE, your math assistant.', width = 35, padx = 2, fg="darkred", font=("Rouge", 18))
label1.place(x = 135, y = 10)

label2 = Label(win, text = 'Write your commands in words and I will work it out!', padx = 2, font=("Rouge", 16))
label2.place(x = 140, y = 60)

label3 = Label(win, text = 'Example- Add 2 and 2', padx = 2, font=("Rouge", 16))
label3.place(x = 250, y = 90)

textfield = StringVar()
entry = Entry(win, width = 50, textvariable = textfield, font=("Rouge", 16))
entry.place(x = 100, y = 150)

button = Button(win, text='Go, Callie!', font=("Rouge", 16), command = calculate)
button.place(x = 270, y = 210)

answer = Listbox(win, height = 3, width = 20, font=("Rouge", 18), fg="darkred")
answer.place(x = 220, y = 250)

win.mainloop()
