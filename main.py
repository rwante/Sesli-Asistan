from komutlar import Komut
import speech_recognition as sr
import tkinter as tk
import pygame                       # pip install pygame


def sesCal():
    # Bip müzik dosyasında bulunan sesi çalar.
    # Bu ses mikrofonun aktif hale geldiğini kullanıcıya bildirmiş olur.
    pygame.mixer.init()
    pygame.mixer.music.load("bip.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def asistan():
    try:
        global root
        root.destroy()
    except:
        pass
    while True:
        sesCal()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=4)
        try:
            data = ""
            data = r.recognize_google(audio, language='tr-TR')
            print(data)
            komut = Komut(data)
            komut.komutBul()
        except sr.UnknownValueError:
            i = "geçici"
            komut = Komut(i)
            komut.seslendirme("Anlayamadım")
        except sr.RequestError:
            i = "geçici"
            komut = Komut(i)
            komut.seslendirme("Sistem çalışmıyor")


root = tk.Tk()
root.image = tk.PhotoImage(file='resim.png')
button = tk.Button(root, image=root.image, bg='white', command=asistan)
root.overrideredirect(True)
root.geometry("120x140+1200+550")
root.wm_attributes("-transparentcolor", "white")
button.pack()
root.mainloop()
