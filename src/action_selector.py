from src.get_SteamVR_path import real_case_path, find_steam_path
from src.check_current_rendermodel import check_current_rendermodel
from src.TouchPlus.touchpro_plus_replace import TouchPro_Plus_Replace
from src.TouchPlus.touchplus_restore import TouchPlus_Restore
from src.TouchQuest2.touchpro_quest2_replace import TouchPro_Quest2_Replace
from src.TouchQuest2.touchquest2_restore import TouchQuest2_Restore
from src.clear import clear

def action_selector():

    headset = None

    while True:

        if not headset:
            
            clear()

            print("Please select an headset : ")
            print("2. Quest 2")
            print("3. Quest 3")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "2":
                    headset = "Quest 2"
                case "3":
                    headset = "Quest 3"
                case "0":
                    clear()
                    exit()
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")
                    headset = None

        elif headset:

            if headset == "Quest 2":
                touch_name = "Touch Quest 2"
            elif headset == "Quest 3":
                touch_name = "Touch Plus"

            clear()

            print(f"Current SteamVR path : {real_case_path(find_steam_path())}\steamapps\common\SteamVR")
            print(f"Current Render Model : {check_current_rendermodel(headset)}\n")

            print("Please make a selection : ")
            print(f"1. Replace {touch_name} Render Models with Touch Pro Render Models")
            print(f"2. Restore {touch_name} Render Models")
            print("3. Switch headset")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "1":
                    if headset == "Quest 2":
                        TouchPro_Quest2_Replace()
                    elif headset == "Quest 3":
                        TouchPro_Plus_Replace()
                case "2":
                    if headset == "Quest 2":
                        TouchQuest2_Restore()
                    elif headset == "Quest 3":
                        TouchPlus_Restore()
                case "3":
                    headset = None
                    continue
                case "0":
                    clear()
                    exit()
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")