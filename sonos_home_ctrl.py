import soco
import csv


def save_cfg(input_list):
    with open('sonos_config.cfg', 'w') as cfg_file:
        csvwriter = csv.writer(cfg_file)
        csvwriter.writerows(input_list)


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


def get_cfg(spk_list):
    output_list = []
    for spk in spk_list:
        output_list.append(get_spk_detail(spk))
    return output_list


def read_cfg(spk_list):
    with open('sonos_config.cfg', 'r') as cfg_file:
        csvfile = csv.reader(cfg_file)
        output_list = list(csvfile)
        return output_list




def main():
    
    all_spk = get_spk_list()

    if all_spk != None:
        print('Speakers detected')
        spk_list = get_cfg(all_spk)
        print(spk_list)
        save_cfg(spk_list)
        




if __name__ == '__main__':
    main()
