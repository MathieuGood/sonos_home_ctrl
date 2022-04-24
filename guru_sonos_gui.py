from tkinter import *
import soco

zlist = (list(soco.discover()))
zlist.sort(key=lambda x: x.ip_address)

for spk in zlist:
    dash = (15 - (len(spk._player_name))) * "-"
    print(spk._player_name, dash, "Vol", spk.volume, "- Treb", spk.treble, "- Bass", spk.bass, '- Loud',
          spk.loudness)

def stat_test():
    for spk in zlist:
        print(spk._player_name, dash, "Vol", spk.volume, "- Treb", spk.treble, "- Bass", spk.bass, '- Loud',
          spk.loudness)

a = stat_test()


window = Tk()

window.title("Guru Sonos Controller")
window.geometry("400x550")
window.minsize(400, 550)
window.iconbitmap("sonos_logo.ico")
window.config(background="#4E5A65")

# CANVAS
width = 400
height = 79
logo_file = PhotoImage(file="sonos_biglogo.png")
logo_canvas = Canvas(window, width=width, height=height, bg="#4E5A65", bd=0, highlightthickness=0)
logo_canvas.create_image(width/2, height/2, image=logo_file)
logo_canvas.pack()

# STATUS FRAME

stat_frame = Frame(window, bg="#4E5A65")

# TITLE

app_title = Label(window, text="Guru Sonos Controller", font=("Courrier", 20), bg="#4E5A65", fg="white")
app_title.pack()

# STATUS LABEL

stat1 = [zlist[0]._player_name, "Vol", zlist[0].volume, "Bass", zlist[0].bass, "Treble", zlist[0].treble]
stat2 = [zlist[1]._player_name, "Vol", zlist[1].volume, "Bass", zlist[1].bass, "Treble", zlist[1].treble]
stat3 = [zlist[2]._player_name, "Vol", zlist[2].volume, "Bass", zlist[2].bass, "Treble", zlist[2].treble]


sonos1 = Label(stat_frame, text=stat1, font=("Courrier", 14), bg="#4E5A65", fg="white")
sonos1.pack()
sonos2 = Label(stat_frame, text=stat2, font=("Courrier", 14), bg="#4E5A65", fg="white")
sonos2.pack()
sonos3 = Label(stat_frame, text=stat3, font=("Courrier", 14), bg="#4E5A65", fg="white")
sonos3.pack()

stat_frame.pack()

window.mainloop()
