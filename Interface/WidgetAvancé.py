import  tkinter
from tkinter import  messagebox

app=tkinter.Tk()
app.geometry("300x350")
#offvalue: quand la case n'est pas coché
#onvalue: quand la case est coché
check_widget=tkinter.Checkbutton(app,text="Publier ", offvalue=2,onvalue=5)

radio_widget=tkinter.Radiobutton(app,text="Homme",value=1)
radio_widget2=tkinter.Radiobutton(app,text="Femme", value=2)

scale_w=tkinter.Scale(app,from_=10,to_=100, tickinterval=25)

spin_w=tkinter.Spinbox(app,from_=1,to_=10)

lb=tkinter.Listbox(app)
lb.insert(1,"Windows")
lb.insert(2,"Linux")
lb.insert(3,"MacOs")

def show_modal_window():
    messagebox.showerror("Erreur","Un problème est survenu!")

def show_modal_info():
    messagebox.showinfo("Informations","C'est bien")

def show_modal_warning():
    messagebox.showwarning("Warning","Attention!")

def show_modal_question():
    messagebox.askquestion("Question","Vous allez bien ?")

def show_modal_cancel():
    messagebox.askokcancel("Question","Voulez vous supprimer ?")

def show_modal_recommencer():
    messagebox.askretrycancel("Recommencer","un problème est survenu voulez vous recommencer?")

btn=tkinter.Button(app,text="Déclencher une erreur",command=show_modal_window)
btn2=tkinter.Button(app,text="Info",command=show_modal_info)
btn3=tkinter.Button(app,text="Warning",command=show_modal_warning)
btn4=tkinter.Button(app,text="Question",command=show_modal_question)
btn5=tkinter.Button(app,text="Cancel",command=show_modal_cancel)
btn6=tkinter.Button(app,text="Recommencer",command=show_modal_recommencer)

btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
check_widget.pack()
radio_widget.pack()
radio_widget2.pack()
scale_w.pack()
spin_w.pack()
lb.pack()
app.mainloop()

