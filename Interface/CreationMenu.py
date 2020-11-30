import tkinter

#cration de la fenetre
window=tkinter.Tk()
window.geometry("500x450")
window.title("Création d'un menu")

def show_about():
    about_window=tkinter.Toplevel(window)
    about_window.title("A propos")


#Menu
menu=tkinter.Menu(window)
firstMenu=tkinter.Menu(menu)

firstMenu.add_command(label="option1")
firstMenu.add_command(label="option2")
firstMenu.add_separator()
firstMenu.add_command(label="Quitter",command=window.quit)

secondMenu=tkinter.Menu(menu)
secondMenu.add_command(label="commande1")
secondMenu.add_command(label="commande2")
secondMenu.add_command(label="A propos",command=show_about)

menu.add_cascade(label="premier",menu=firstMenu)
menu.add_cascade(label="deuxième",menu=secondMenu)

window.config(menu=menu)
window.mainloop()