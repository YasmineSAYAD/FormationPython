from random import randint, choice
from tkinter import *
import string

def generate_password():
    password_min=6
    password_max = 12
    all_chars=string.ascii_letters+string.punctuation+string.digits
    password= "".join(choice(all_chars) for x in range(randint(password_min,password_max)))



    password_entry.delete(0,END)
    password_entry.insert(0,password)

#creer la fenetre
window=Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("logo.ico")
window.config(background="#0000ff")

#creer la frame principale
frame=Frame(window,bg='#0000ff')

#creation d'image
width=300
height=300
image=PhotoImage(file="user.png").zoom(35).subsample(32)

#canvas c'est un espace ou on peut dessiner des composants graphiques
canvas=Canvas(frame,width=width, height=height,bg='#0000ff',bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W) #W west

#creer une sous boite
right_frame=Frame(frame,bg='#0000ff')
right_frame.grid(row=0, column=1, sticky=W)
#creer un titre
label_title=Label(right_frame,text="Mot de passe", font=("Helvetica",20),bg='#0000ff',fg='white')
label_title.pack()

#creer un champ
password_entry=Entry(right_frame, font=("Helvetica",20),bg='#0000ff',fg='white')
password_entry.pack()

#creer un titre
bouton=Button(right_frame,text="Génerer", font=("Helvetica",20),bg='#0000ff',fg='white', command=generate_password)
bouton.pack(fill=X)


#afficher la frame
frame.pack(expand=YES)

#creer une barre de menu
menu_bar=Menu(window)
#creer un  premier menu
file_menu=Menu(menu_bar,tearoff=0)
#tearofff=0~pour eviter d'avoir des tiret
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier",menu=file_menu)

#configuer la fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

#afficher la fenetre
window.mainloop()