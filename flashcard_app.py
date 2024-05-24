from tkinter import *
from random import randint

root = Tk()
root.title("English-Lithuanian Flash Cards for Kaihan")
root.geometry("550x500")

words = [
    ("Labas", "Hello"),
    ("Viso Gero", "Good Bye"),
    ("Prašau", "Please"),
    ("Ačiū", "Thank You"),
    ("Atsiprašau", "Sorry"),
    ("Taip", "Yes"),
    ("Ne", "No"),
    ("Kas", "Who"),
    ("Ką", "What"),
    ("Kodėl", "Why"),
    ("Kur", "Where"),
    ("Galbūt", "Maybe"),
    ("Padėk", "Help"),
    ("Draugas", "Friend"),
    ("Šeima", "Family"),
    ("Meilė", "Love"),
    ("Maistas", "Food"),
    ("Vanduo", "Water"),
    ("Namai", "Home"),
    ("Darbas", "Work"),
    ("Mokykla", "School"),
    ("Laikas", "Time"),
    ("Kompiuteris", "Computer"),
    ("Diena", "Day"),
    ("Naktis", "Night"),
    ("Rytas", "Morning"),
    ("Pietūs", "Lunch"),
    ("Mašina", "Car"),
    ("Katinas", "Cat"),
    ("Šuo", "Dog"),
    ("Pinigai", "Money"),
    ("Gerai", "Alright"),
    ("Geras", "Good"),
    ("Blogas", "Bad"),
    ("Klausyk", "Listen"),
    ("Valgyk", "Eat"),
    ("Gražus", "Beautiful"),
    ("Mieloji", "Sweetheart"),
    ("Angelas", "Angel"),
    ("Žavinga", "Adorable"),
    ("Medus", "Honey"),
    ("Lobis", "Treasure"),
    ("Žaidimas", "Game"),
]

count = len(words)

def next():
    global hinter, hint_count
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0, count-1)
    lithuanian_word.config(text=words[random_word][0])
def answer():
    if my_entry.get().lower() == words[random_word][1].lower():
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().lower()}. The word is {words[random_word][1]}")

hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1] [hint_count]
        hint_label.config(text=hinter)
        hint_count += 1

def flip_words():
    global words, random_word
    words[random_word] = (words[random_word][1], words[random_word][0])
    lithuanian_word.config(text=words[random_word][0])

lithuanian_word = Label(root, text="", font=("Helvetica", 36))
lithuanian_word.pack(pady = 50)

answer_label = Label(root, text="")
answer_label.pack(pady = 20)
hint_label = Label(root, text="")
hint_label.pack(pady = 20)
my_entry = Entry(root, font="Helvetica, 18")
my_entry.pack(pady = 20)
button_frames = Frame(root)
button_frames.pack(pady = 20)
answer_button = Button(button_frames, text="Answer", command = answer)
answer_button.grid (row = 0, column = 1, padx= 20)
next_button = Button(button_frames, text="Next", command= next)
next_button.grid(row = 0, column = 2)
hint_buton = Button(button_frames, text = "Hint", command = hint)
hint_buton.grid(row = 0, column = 3, padx = 20)
flip_button = Button(button_frames, text="Flip", command=flip_words)
flip_button.grid(row=0, column=4, padx=20)

next()
root.mainloop()