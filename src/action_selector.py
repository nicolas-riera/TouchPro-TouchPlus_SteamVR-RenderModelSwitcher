from src.get_SteamVR_path import real_case_path, find_steam_path
from src.check_current_rendermodel import check_current_rendermodel
from src.TouchPlus.touchpro_plus_replace import TouchPro_Plus_Replace
from src.TouchPlus.touchplus_restore import TouchPlus_Restore
from src.clear import clear

def action_selector():

    while True:

        clear()

        print(f"Current SteamVR path : {real_case_path(find_steam_path())}\steamapps\common\SteamVR")
        print(f"Current Render Model : {check_current_rendermodel()}\n")

        print("Please make a selection : ")
        print("1. Replace Touch Plus Render Models with Touch Pro Render Models")
        print("2. Restore Touch Plus Render Models")
        print("0. Exit")

        usr_choice = input()

        match usr_choice:
            case "1":
                TouchPro_Plus_Replace()
            case "2":
                TouchPlus_Restore()
            case "0":
                clear()
                exit()
            case _:
                clear()
                print("Invalid Choice.")
                input("Press Enter to Continue.")