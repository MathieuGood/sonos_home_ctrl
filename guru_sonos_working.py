import soco
from soco.discovery import by_name

# Attributing a variable to each Sonos speaker object
front = by_name("Salon")
back = by_name("Cuisine")
side = by_name("Salle à manger")


zlist = list(soco.discover())
zlist.sort(key=lambda x: x.ip_address)

max_length = max(len(str(s._player_name)) for s in zlist)
line_length = max_length + 41
sep_line = line_length * "#"
unch = "level unchanged"
guru_error = "That's not what I call a proper quest... Try again!\n"

def name_box_length(spk):
    namebox_l = (line_length - 39 - (len(spk._player_name)))
    return namebox_l


def dash(namebox_l):
    namebox_dash = namebox_l * "-"
    return namebox_dash


def tab(namebox_l):
    namebox_tab = (namebox_l + 6) * ">"
    return namebox_tab


# Displaying name, volume level, treble level, bass level and loudness status of each speaker
def print_status():
    print(sep_line)
    for spk in zlist:
        print(spk._player_name, dash(name_box_length(spk)), "Vol", spk.volume,
              "- Treb", spk.treble, "- Bass", spk.bass, '- Loud', spk.loudness)
        if spk.night_mode is not None:
            if spk.night_mode is False:
                night_stat = "OFF"
            else:
                night_stat = "ON"
        if spk.dialog_mode is not None:
            if front.dialog_mode is False:
                dialog_stat = "OFF"
            else:
                dialog_stat = "ON"
            print(tab(name_box_length(spk)), "Dialog :", dialog_stat, "     Night :", night_stat)
    print(sep_line)



def spk_vol():
    for spk in zlist:
        print(spk._player_name, dash(name_box_length(spk)), "Vol", spk.volume)
        try:
            spk.volume = int(input("Enter volume level >>> "))
        except:
            print("Volume", unch)

def bass_lvl():
    for spk in zlist:
        print(spk._player_name, dash(name_box_length(spk)), "Bass", spk.bass)
        try:
            spk.bass = int(input("Enter bass level >>> "))
        except:
            print("Bass", unch)

def treble_lvl():
    for spk in zlist:
        print(spk._player_name, dash(name_box_length(spk)), "Treb", spk.treble)
        try:
            spk.treble = int(input("Enter treble level >>> "))
        except:
            print("Treble", unch)

def loudness_off():
    for spk in zlist:
        spk.loudness = False

def loudness_on():
    for spk in zlist:
        spk.loudness = True

def usual_eq():
    loudness_on()
    front.treble = 3
    front.bass = 5
    back.treble = 3
    back.bass = 6
    side.treble = 4
    side.bass = 7
    for spk in zlist:
        if spk.night_mode is not None:
            spk.night_mode = False


def silent_mode():
    loudness_off()
    for spk in zlist:
        spk.treble = 3
        spk.bass = 3
        if spk.night_mode is not None:
            spk.night_mode = True

def master_vol():
    try:
        v = input("How much?")
        if v == "":
            v = front.volume
        else:
            v = int(v)
        volume_balance(v)
    except:
        print(guru_error)

def volume_balance(v):
    front.volume = v
    back.volume = v * 1.1
    side.volume = v * 0.8


def dialog_switch():
    for spk in zlist:
        if spk.dialog_mode is not None:
            if spk.dialog_mode is True:
                spk.dialog_mode = False
            else:
                spk.dialog_mode = True

def gurumenu():
    print_status()
    menu = [["(L) Loudness on",
            "  (O) Loudness off"],
            ["(U) Usual EQ",
            "     (N) Night mode"],
            ["(D) Dialog mode",
            "  (M) Master volume"],
            ["(B) Bass level",
             "   (T) Treble level"],
            ["(V) Volume level",
            " (E) Exit program"]]
    for choice in menu:
        print(" " * 6, *choice)
    menuchoice = str(input("\nWhat is your quest?\n"))
    menuchoice = menuchoice.upper()
    if menuchoice == "O":
        loudness_off()
    elif menuchoice == "L":
        loudness_on()
    elif menuchoice == "U":
        usual_eq()
    elif menuchoice == "N":
        silent_mode()
    elif menuchoice == "M":
        master_vol()
    elif menuchoice == "D":
        dialog_switch()
    elif menuchoice == "V":
        spk_vol()
    elif menuchoice == "B":
        bass_lvl()
    elif menuchoice == "T":
        treble_lvl()
    elif menuchoice == "E":
        print("ヾ(＾-＾)ノ See you later alligator!")
        quit()
    else:
        try:
            v = int(menuchoice)
            volume_balance(v)
        except:
            print(guru_error)
    gurumenu()

gurumenu()
