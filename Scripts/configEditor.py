import json
import os
import saveImage as save


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def ClearSources():
    f = open('config.json')
    data = json.load(f)
    f.close()
    data['sources'] = []
    with open("config.json", "w") as outfile:
        json.dump(data, outfile)
    Main()


def SaveNewImages():
    f = open('config.json')
    data = json.load(f)
    f.close()
    if data['save_all_new']:
        data['save_all_new'] = False
    else:
        data['save_all_new'] = True
    with open("config.json", "w") as outfile:
        json.dump(data, outfile)
    Main()


def AskCollectionNextTime():
    f = open('config.json')
    data = json.load(f)
    f.close()
    if data['ask_for_collection']:
        data['ask_for_collection'] = False
    else:
        data['ask_for_collection'] = True
    with open("config.json", "w") as outfile:
        json.dump(data, outfile)
    Main()


def ClearSourceOnCollection():
    f = open('config.json')
    data = json.load(f)
    f.close()
    if data['clear_on_new_collection']:
        data['clear_on_new_collection'] = False
    else:
        data['clear_on_new_collection'] = True
    with open("config.json", "w") as outfile:
        json.dump(data, outfile)
    Main()


def UseSave():
    f = open('config.json')
    data = json.load(f)
    f.close()
    if data['use_save']:
        data['use_save'] = False
    else:
        data['use_save'] = True
    with open("config.json", "w") as outfile:
        json.dump(data, outfile)
    Main()


def ViewSources():
    f = open('config.json')
    data = json.load(f)
    f.close()
    for source in data['sources']:
        print(Colors.WARNING + source)
    input()
    Main()


def Main():
    f = open('config.json')
    data = json.load(f)
    f.close()
    os.system('cls')
    print(Colors.RESET + "Collection: " + Colors.CYAN + data['collection'][1:])
    if data['save_all_new']:
        print(Colors.RESET + '1    Save New Backgrounds: ' + Colors.GREEN + "TRUE")
    else:
        print(Colors.RESET + "1    Save New Backgrounds: " + Colors.FAIL + "FALSE")
    if data['use_save']:
        print(Colors.RESET + '2    Use Saved: ' + Colors.GREEN + "TRUE")
    else:
        print(Colors.RESET + "2    Use Saved: " + Colors.FAIL + "FALSE")
    if data['ask_for_collection']:
        print(Colors.RESET + '3    Ask For Collection: ' + Colors.GREEN + "TRUE")
    else:
        print(Colors.RESET + "3    Ask For Collection: " + Colors.FAIL + "FALSE")
    if data['clear_on_new_collection']:
        print(Colors.RESET + '4    Clear Sources On New Collection: ' + Colors.GREEN + "TRUE")
    else:
        print(Colors.RESET + "4    Clear Sources On New Collection: " + Colors.FAIL + "FALSE")
    print(Colors.RESET + "5    Reset Sources")
    print(Colors.RESET + "6    View Sources")
    print(Colors.RESET + "7    Save Current Background")
    print(Colors.RESET + "99   Quit")

    usr = input(Colors.RESET + '-> ')
    if usr.isdigit():
        usr = int(usr)
    else:
        Main()

    match usr:
        case 1:
            SaveNewImages()
        case 2:
            UseSave()
        case 3:
            AskCollectionNextTime()
        case 4:
            ClearSourceOnCollection()
        case 5:
            ClearSources()
        case 6:
            ViewSources()
        case 7:
            save.run()
            Main()
        case 99:
            exit()
        case _:
            Main()


if __name__ == "__main__":
    Main()
