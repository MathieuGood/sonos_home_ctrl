import soco


def get_spk_list():
    spk_list = soco.discover()
    if spk_list != None:
        return list(spk_list)
    else:
        return "No Sonos speakers detected on this network"

def get_spk_detail(spk):
    name = spk.player_name
    ip = spk.ip_address
    return name, ip

    # return name and ip of speaker (and group?)


def main():
    all_spk = get_spk_list()

    for one in all_spk:
        print(get_spk_detail(one))




if __name__ == '__main__':
    main()
