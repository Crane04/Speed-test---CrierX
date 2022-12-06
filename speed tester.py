from tkinter import *
import tkinter.messagebox as tkm
import six_lettered_word
import random
root = Tk()
root.title("CrierX")
words = six_lettered_word.arr
root.geometry("350x170")
question = Label(root, text=random.choice(words).lower())
answer_field = Entry(root, width=45)
time_label = Label(root)
num = 5
score = 0
score_sheet = Label(root, text="Score: " + str(score))
score_sheet.pack()


def start():
    global num, score
    if num > 0:
        num -= 1
        time_label.configure(text=num)
        question.pack()
        answer_field.pack()
        time_label.pack()
        root.after(1000, start)
        button.configure(text='Quit', command=root.quit)
        root.bind("<Return>", st)
    elif num <= 0:
        time_label.configure(text="Time Up!")
        tkm.showinfo("CrierX", f"Game Ended.\n You got {score} points")
        answer_field.configure(state=DISABLED)
        root.quit()


def nxt():
    global num, score
    question.configure(text=random.choice(words).lower())
    num = num + 2
    time_label.configure(text=num)
    score += 1
    score_sheet.configure(text="Score: "+str(score))


def st(event):
    global score
    if question.cget("text") != answer_field.get():
        time_label.configure(text="You Lost!")
        answer_field.configure(state=DISABLED)
        tkm.showinfo("CrierX", f"You typed the wrong Word and had {score} points.\nTry Again")
        root.quit()
    else:
        answer_field.delete(0, END)
        answer_field.insert(0, "")
        nxt()


button = Button(root, text="Start", command=start)
button.pack()
root.mainloop()
