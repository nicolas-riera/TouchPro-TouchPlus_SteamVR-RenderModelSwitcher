import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_LEFT = os.path.join(BASE_DIR, "..", "assets", "TouchPlus_Models", "oculus_quest_plus_controller_left")
SOURCE_RIGHT = os.path.join(BASE_DIR, "..", "assets", "TouchPlus_Models", "oculus_quest_plus_controller_right")

DESTINATION_LEFT = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_left"))
DESTINATION_RIGHT = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_right"))

def TouchPlus_Restore():

    clear()

    if os.path.exists(DESTINATION_LEFT):
        shutil.rmtree(DESTINATION_LEFT)
    if os.path.exists(DESTINATION_RIGHT):
        shutil.rmtree(DESTINATION_RIGHT)

    shutil.copytree(SOURCE_LEFT, DESTINATION_LEFT)
    shutil.copytree(SOURCE_RIGHT, DESTINATION_RIGHT)

    print("Restoring done.")
    input("Press Enter to continue.")