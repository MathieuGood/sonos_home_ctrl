import soco
from soco import SoCo
import csv
import json

# Global variables
config_file = 'sonos_cfg.json'


def menu():

    print('\n🔈 Sonos Home Control 🔈\n')


def get_spk_list():
    spk_list = soco.discover()
    if spk_list != None:
        return list(spk_list)
    else:
        exit("No Sonos speakers detected on this network")


def get_spk_detail(spk):
    name = spk.player_name
    ip = spk.ip_address
    vol = spk.volume
    bass = spk.bass
    treb = spk.treble
    return [name, {'ip': ip, 'vol': vol, 'bass': bass, 'treb': treb}]


def get_cfg(spk_list):
    output_list = []
    for spk in spk_list:
        spk_detail = get_spk_detail(spk)
        output_list.append(spk_detail)
    print(output_list)
    return output_list


def write_cfg(list_cfg, file=config_file):
    json_cfg = json.dumps(list_cfg, indent=4, ensure_ascii=False)
    with open(file, "w") as outfile:
        outfile.write(json_cfg)


def open_cfg(file=config_file):
    a = input('Wait')
    with open(file, 'r') as json_file:
        return json.load(json_file)


def load_cfg(cfg):
    cfg_out = []
    for spk in cfg:
        cfg_out.append([spk[0], spk[1]])
    print(cfg_out)
    return cfg_out


def set_cfg(cfg):
    for spk in cfg:
        s = SoCo(spk[1]['ip'])
        s.bass = spk[1]['bass']
        s.treble = spk[1]['treb']


def choose_spk(spk_list):
    print("Which speaker ?")
    for count, spk in enumerate(spk_list):
        print(f'{count+1}. {spk.player_name}')
    chosen_spk = int(input('Enter speaker number : ')) - 1
    return spk_list[chosen_spk]


def set_balance_cfg(spk_list):
    print('Select master speaker :')
    master = choose_spk(spk_list)
    balance_cfg = [[master, 1]]
    for spk in spk_list:
        if spk != master:
            multi = float(input(f'Enter volume multiplier for {spk.player_name}'))
            balance_cfg.append([spk, multi])
    print(balance_cfg)
    return balance_cfg
    

def set_spk_balance(balance_cfg):
    master_vol = balance_cfg[0][0].volume
    for spk in balance_cfg:
        print(spk)
        spk[0].volume = round(spk[1] * master_vol)


def main():
    
    all_spk = get_spk_list()

    spk_cfg = get_cfg(all_spk)
 
    write_cfg(spk_cfg)

    menu()

    config = open_cfg()

    set_cfg(load_cfg(config))

    # balance_cfg = set_balance_cfg(all_spk)
    # set_spk_balance(balance_cfg)



if __name__ == '__main__':
    main()
