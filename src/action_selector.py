from src.get_SteamVR_path import real_case_path, find_steam_path
from src.check_current_rendermodel import check_current_rendermodel
from src.TouchPlus.touchpro_plus_replace import TouchPro_Plus_Replace
from src.TouchPlus.touchplus_restore import TouchPlus_Restore
from src.TouchQuest2.touchpro_quest2_replace import TouchPro_Quest2_Replace
from src.TouchQuest2.touchquest2_restore import TouchQuest2_Restore
from src.wands.vive_2_set import Vive_2_set
from src.wands.vive_1_set import Vive_1_set
from src.clear import clear

def action_selector():

    device = None

    while True:

        if not device:
            
            clear()

            print("Please select a device : ")
            print("1. Vive Controllers")
            print("2. Quest 2 Controllers/Touch Quest 2")
            print("3. Quest 3 Controllers/Touch Plus")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "1":
                    device = "Wands"
                case "2":
                    device = "Quest 2"
                case "3":
                    device = "Quest 3"
                case "0":
                    clear()
                    break
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")
                    device = None

        elif device:

            if device == "Quest 2":
                touch_name = "Touch Quest 2"
            elif device == "Quest 3":
                touch_name = "Touch Plus"
            elif device == "Wands":
                text_1 = "Use Vive Controller 2.0 Render Model"
                text_2 = "Use Vive Controller 1.0 Render Model"

            clear()

            print(f"Current SteamVR path : {real_case_path(find_steam_path())}\steamapps\common\SteamVR")
            print(f"Current Render Model : {check_current_rendermodel(device)}\n")

            print("Please make a selection : ")
            if device == "Quest 2" or device == "Quest 3":
                print(f"1. Replace {touch_name} Render Models with Touch Pro Render Models")
                print(f"2. Restore {touch_name} Render Models")
            else:
                print(f"1. {text_1}")
                print(f"2. {text_2}")
            print("3. Switch device")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "1":
                    if device == "Quest 2":
                        TouchPro_Quest2_Replace()
                    elif device == "Quest 3":
                        TouchPro_Plus_Replace()
                    elif device == "Wands":
                        Vive_2_set()
                case "2":
                    if device == "Quest 2":
                        TouchQuest2_Restore()
                    elif device == "Quest 3":
                        TouchPlus_Restore()
                    elif device == "Wands":
                        Vive_1_set()
                case "3":
                    device = None
                    continue
                case "0":
                    clear()
                    break
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")