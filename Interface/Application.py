from tkinter import *
import webbrowser

def open_channel():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")

# créer une fenêtre
window=Tk()
#personnaliser cette fenetre
window.title("My Application")
window.geometry("1080x740")
#taille minimale
window.minsize(480,360)
window.iconbitmap("logo.ico")
window.config(background='#0000ff')

#creer la frame exemple: frame=Frame(window,bg='#0000ff',bd=1, relief=SUNKEN)
frame=Frame(window,bg='#0000ff')

#ajouter un premier texte
label_title=Label(frame,text="Bienvenue sur l'application",font=("Courrier",40),bg='#0000ff',fg='white')
#pour jouer sur la position pack(side=LEFT/RIGHT...)
label_title.pack()

#Ajouter un second texte
label_subtitle=Label(frame,text="Salut à tous",font=("Courrier",25),bg='#0000ff',fg='white')
label_subtitle.pack()

#ajouter un premier bouton
pr_button=Button(frame,text="Ouvrir Youtube",font=("Courrier",25),bg='white',fg='#0000ff', command=open_channel)
pr_button.pack(pady=25,fill=X)   #fill=X remplissage sur X, pady=25 marge en Y

#ajouter la frame
#expand=YES pour centrer
frame.pack(expand=YES)


#taille maximale
# Afficher
window.mainloop()
