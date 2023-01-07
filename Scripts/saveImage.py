import shutil
import os

host = "saved"


def run():
    for i in range(999):
        name = host
        name += str(i)
        name += ".jpg"
        if not os.path.exists("..\\saved\\" + name):
            shutil.copyfile("..\\random_wallpaper.jpg", name)
            shutil.move(name, "..\\saved\\" + name)
            break


if __name__ == "__main__":
    run()
