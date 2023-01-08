# Background Image Refresh (BIR)
This allows you to have the ability of changing your computer wallpaper every time you login in. Have a change of appearance and get rid of the boring repetitiveness.


## Folder Path
```
BackgroundImageRefresh
│   README.md
│   random_wallpaper.jpg   
│   Save.bat   
│   ConfigEditor.bat   
│
└───venv
│   │   ...
│   │
│   └───Scripts
│       │   ...
│       │   pythonw.exe
│       │   ...
│   
└───Scripts
│   │   config.json
│   │   configEditor.py
│   │   main.pyw
│   │   saveImage.py
│   
└───saved
    │   saved0.jpg
    │   ...
```

## Scripts
### Files/Folders
- `random_wallpaper.jpg` is for the random picture from the internet
- `pythonw.exe` is to run the script with the modules installed
- `Scripts` contains the source for this project
- `saved` will contain all the saved wallpapers

### .bat Scripts
- `Run.bat` will run the program once
- `Config.bat` will run the config editor
- `Save.bat` will save the current wallpaper once

## Config
- `collection` the collection name that is retrieved from the url
- `save_all_new` will keep track if you want to save all the new genertated wallpapers
- `use_save` will keep track if we use saved wallpapers
- `clear_on_new_collection` if we get rid of all the sources when putting in a new collection. Useful if you want mulitple collections to randomize from.
- `ask_for_collection` if this is true will ask the user for a collection to use as a generated source
- `sources` is a list of all the image's url to pull from

## Customization
1. Head to [Wallpaperaccess.com](https://wallpaperaccess.com/) and find a collection of photo's that you like. 
2. The url `https://wallpaperaccess.com/corvette` take the part after the last \ in this case `corvette`
3. When prompted enter the text, including the dashes

## Setup
### Setting up
1. Download the lastest release
2. Double click `Config.bat` to set up your choices 
3. Default Config settings
   1. Save All New - False
   2. Use Save - False
   3. Clear On New Collection - True
   4. Ask For Collection - True
   5. Sources - Empty
4. Remove `saved0.jpg` from `saved` (is there as a default)

**Leave Ask For Collection alone, will be set to False after every time a name is entered**

### Creating a scheduled run
- Open Task Scheduler
- Create new task (right side)
- Add a name 
- Go to triggers
- Create a trigger for when you want to run the background change
- Go to actions
  - For Program/Script paste the project path + `venv\Scripts\pythonw.exe`
  - For agruments add `main.pyw`
  - For start in paste the project path `C:\some\path\to\Bacgkround-Image-Refresh-1.0.0`
- Go to Conditions
- Uncheck all power options
- Click ok
