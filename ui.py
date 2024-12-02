from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain ):
        self.quiz = quiz_brain
        self.window=Tk()
        self.window.title="Quizzler"
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_text=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_text.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text= self.canvas.create_text(150,125,width=280,text="Some Question Text", fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)


        true_image= PhotoImage(file="./images/true.png")
        self.true_button=Button(image=true_image, highlightthickness=0,command=self.Check_awnser_True)
        false_image= PhotoImage(file="./images/false.png")
        self.false_button=Button(image=false_image, highlightthickness=0,command=self.Check_awnser_False)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
       
        
    def Check_awnser_True(self):
        self.Feed_back(self.quiz.check_answer("True"))
    def Check_awnser_False(self):
        self.Feed_back(self.quiz.check_answer("False"))
    def Feed_back(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
