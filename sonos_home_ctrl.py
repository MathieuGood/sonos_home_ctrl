import soco
import csv

# Global variables
config_file = 'sonos_config.cfg'


def menu():

    print('\n🔈 Sonos Home Control 🔈\n')



def save_cfg(input_list):
    with open(config_file, 'w') as cfg_file:
        csvwriter = csv.writer(cfg_file)
        csvwriter.writerows(input_list)


def get_spk_list():
    spk_list = soco.discover()
    if spk_list != None:
        return list(spk_list)
    else:
        exit("No Sonos speakers detected on this network")


def get_spk_detail(spk):
    name = spk.player_name
    ip = spk.ip_address
    return name, ip


def get_cfg(spk_list):
    output_list = []
    for spk in spk_list:
        output_list.append(get_spk_detail(spk))
    return output_list


def read_cfg(config_file):
    with open(config_file, 'r') as cfg_file:
        csvfile = csv.reader(cfg_file)
        output_list = list(csvfile)
        return output_list


def load_cfg(config_file):
    for spk in config_file:
        spk[0]



def choose_spk(spk_list):
    print("Which speaker ?")
    for count, spk in enumerate(spk_list):
        print(f'{count+1}. {spk.player_name}')
    chosen_spk = int(input('Enter speaker number : ')) - 1
    return spk_list[chosen_spk]


def set_balance_cfg(spk_list):
    master = choose_spk(spk_list)
    balance_cfg = [[master, 1]]
    for spk in spk_list:
        if spk != master:
            multi = float(input(f'Enter volume multiplicator for {spk.player_name}'))
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

    menu()

    balance_cfg = set_balance_cfg(all_spk)
    set_spk_balance(balance_cfg)

    spk_cfg = get_cfg(all_spk)
    save_cfg(spk_cfg)




if __name__ == '__main__':
    main()
