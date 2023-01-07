# Background Image Refresh (BIR)

## Config


## Customization
- Head to [Wallpaperaccess.com](https://wallpaperaccess.com/) and find a collection of photo's that you like. 
- Change the `collection_name`[^1] to the url collection name you have choosen. 

[^1]: Keep the `/`. My current collection name is `corvette`

## Setup
- Open Task Scheduler
- Create new task (right side)
- Add a name 
- Go to triggers
- Create a trigger for log on and another for workstation unlock
- Go to actions
  - For Program/Script paste the cmd link
  - For agruments add `background.py`
  - For start in paste the folder path that contains the .py script
- Go to Conditions
- Uncheck all power options
- Check the network connection
- Click ok

Done!!! :smiley:

## To do
1. Allow users to pick options from a list
2. Only happen if user has setting enabled
3. more to be thought of...