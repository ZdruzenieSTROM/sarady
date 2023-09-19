import tkinter

window = tkinter.Tk()
window.title("Šarády")
window.attributes("-topmost", 1, "-fullscreen", 1)
w_width = window.winfo_screenwidth()
w_height = window.winfo_screenheight()
canvas = tkinter.Canvas(window, height=w_height, width=w_width, bg="white")
canvas.pack()

# ulozenie slov z suborov do listov
lahke, stredne, tazke, veducovske = [], [], [], []

with open("lahke.txt", "r", encoding="utf-8") as file_lahke:
    for i in file_lahke:
        lahke.append(i.strip().upper())

with open("stredne.txt", "r", encoding="utf-8") as file_stredne:
    for i in file_stredne:
        stredne.append(i.strip().upper())

with open("tazke.txt", "r", encoding="utf-8") as file_tazke:
    for i in file_tazke:
        tazke.append(i.strip().upper())

with open("veducovske.txt", "r", encoding="utf-8") as file_veducovske:
    for i in file_veducovske:
        veducovske.append(i.strip().upper())

# obrazky
img_rici = tkinter.PhotoImage(file='evolucia sarad_rici.gif')
img_matus = tkinter.PhotoImage(file='evolucia sarad_matus.gif')
img_michal = tkinter.PhotoImage(file='evolucia sarad_michal.gif')
img_martin = tkinter.PhotoImage(file='evolucia sarad_martin.gif')


# premenne
hra = 0
body = 0


def spusti():
    global word, difficulty
    canvas.delete("volba")
    vid_win = canvas.create_window(
        w_width//4, w_height//2+w_height//3, window=t_win, tag="tlacidlo")
    vid_loose = canvas.create_window(
        w_width//4+w_width//2, w_height//2+w_height//3, window=t_loose, tag="tlacidlo")
    canvas.create_text(w_width//2, w_height//2, text=word,
                       font=f'Comfortaa {w_width//50}', anchor="center", tag="tlacidlo")


def klik(event):
    global x, y, word, difficulty, hra
    if hra == 0:
        x, y = event.x, event.y
        if x < w_width//4:
            if len(lahke) > 0:
                canvas.delete("obrazok")
                word = lahke[0]
                difficulty = "lahke"
                spusti()
                hra = 1
        elif x >= w_width//4 and x <= w_width//2:
            if len(stredne) > 0:
                canvas.delete("obrazok")
                word = stredne[0]
                difficulty = "stredne"
                spusti()
                hra = 1
        elif x >= w_width//2 and x <= w_width//4*3:
            if len(tazke) > 0:
                canvas.delete("obrazok")
                word = tazke[0]
                difficulty = "tazke"
                spusti()
                hra = 1
        else:
            if len(veducovske) > 0:
                canvas.delete("obrazok")
                word = veducovske[0]
                difficulty = "veducovske"
                spusti()
                hra = 1


def win():
    global hra, body, word, difficulty
    if difficulty == "lahke":
        body += 1
        lahke.pop(0)
    elif difficulty == "stredne":
        body += 3
        stredne.pop(0)
    elif difficulty == "tazke":
        body += 5
        tazke.pop(0)
    else:
        body += 7
        veducovske.pop(0)
    canvas.delete("tlacidlo")
    hra = 0
    menu()


def loose():
    global hra, word, difficulty
    if difficulty == "lahke":
        lahke.pop(0)
    elif difficulty == "stredne":
        stredne.pop(0)
    elif difficulty == "tazke":
        tazke.pop(0)
    else:
        veducovske.pop(0)
    canvas.delete("tlacidlo")
    hra = 0
    menu()


def menu():
    # print(lahke)
    # print(len(lahke))
    if len(lahke) > 0:
        canvas.create_image(w_width//8, w_height//2+175,
                            image=img_rici, tag="obrazok")
    else:
        canvas.create_text(w_width//8, w_height//2, text="ĽAHKÉ DOŠLI",
                           font=f'Comfortaa {w_width//70}', anchor="center", tag="obrazok")
    if len(stredne) > 0:
        canvas.create_image(w_width//8*3, w_height//2,
                            image=img_matus, tag="obrazok")
    else:
        canvas.create_text(w_width//8*3, w_height//2, text="STREDNÉ DOŠLI",
                           font=f'Comfortaa {w_width//70}', anchor="center", tag="obrazok")
    if len(tazke) > 0:
        canvas.create_image(w_width//8*5, w_height//2,
                            image=img_michal, tag="obrazok")
    else:
        canvas.create_text(w_width//8*5, w_height//2, text="ŤAŽKÉ DOŠLI",
                           font=f'Comfortaa {w_width//70}', anchor="center", tag="obrazok")
    if len(veducovske) > 0:
        canvas.create_image(w_width//8*7, w_height//2-50,
                            image=img_martin, tag="obrazok")
    else:
        canvas.create_text(w_width//8*7, w_height//2, text="VEDÚCOVSKÉ DOŠLI",
                           font=f'Comfortaa {w_width//70}', anchor="center", tag="obrazok")


def ukonci():
    global hra, body
    hra = 1
    canvas.delete("obrazok")
    canvas.delete("tlacidlo")
    canvas.delete("koniec")
    canvas.create_text(w_width//2, w_height//2,
                       text=f'VÝSLEDNÝ POČET BODOV: {str(body)}', font=f'Comfortaa {w_width//50}', anchor="center")
    file_body = open("body.txt", "w", encoding="utf-8")
    file_body.write(f'VÝSLEDNÝ POČET BODOV: '+str(body))
    vid_zavri = canvas.create_window(
        w_width//2, 30, window=t_zavri, tag="koniec")


def zavri():
    window.destroy()


# tlacidla
t_ukonci = tkinter.Button(canvas, text="UKONČI HRU",
                          font="Comfortaa 24", width=12, command=ukonci)
t_zavri = tkinter.Button(canvas, text="ZAVRI OKNO",
                         font="Comfortaa 24", width=12, command=zavri)
t_win = tkinter.Button(canvas, text="VYŠARÁDIL", font="Comfortaa 24",
                       width=12, command=win, background="light green")
t_loose = tkinter.Button(canvas, text="NEVYŠARÁDIL", font="Comfortaa 24",
                         width=12, command=loose, background="light coral")
# t_win=tkinter.Button(canvas,text="Vyšarádil",background="light green")
# t_loose=tkinter.Button(canvas,text="Nevyšarádil",background="light coral")

# nabindovanie
canvas.bind("<Button-1>", klik)

# tlacidlo na ukoncenie
vid_ukonci = canvas.create_window(
    w_width//2, 30, window=t_ukonci, tag="koniec")

menu()
canvas.mainloop()
