import soco


def get_spk_list():
    spk_list = soco.discover()
    if spk_list != None:
        return list(spk_list)
    else:
        return "No Sonos speakers detected on this network"

def get_spk_detail(spk):
    ...
    # return name and ip of speaker (and group?)


def main():
    print(get_spk_list())



if __name__ == '__main__':
    main()
