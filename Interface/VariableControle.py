import tkinter

"""
StringVar(): chaine de caractères[str]
IntVar(): nombre entier[int]
DoubleVar(): nombre flottant[float]
BooleanVar(): booleen[bool] // 1 si vrai, 0 sinon
"""


# creer un observateur
def update_label(*args):
    var_label.set(var_entry.get())


def update(*args):
  if var.get():
    print("c'est un homme")
  else:
    print("c'est une femme")


window = tkinter.Tk()
window.geometry("400x400")
window.title("Variables tkinter")

var_label = tkinter.StringVar()
# connecter var_label et label
label = tkinter.Label(window, text="", width=20, textvariable=var_label)
# affecter une valeur à var_label pour l'afficher
var_label.set("Coucou")

# champ de saisi
var_entry = tkinter.StringVar()
# r c'est le mode: observateur va être appelé à chaque fois queque la variable change
# u c'est le mode qui sert à supprimer la variable
# w  c'est le mode quand utilise quand la valeur est modifiée
# var_entry.trace("w",update_label()): surveiller var_entry quand on fait la modification
var_entry.trace("w", update_label)
entry = tkinter.Entry(window, textvariable=var_entry)

var=tkinter.IntVar()
var.trace("w",update)
radio1=tkinter.Radiobutton(window,text="Homme",value=1,variable=var)
radio2=tkinter.Radiobutton(window,text="Femme",value=0,variable=var)

radio1.pack()
radio2.pack()
label.pack()
entry.pack()

window.mainloop()
