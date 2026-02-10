import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE = os.path.join(BASE_DIR, "..", "..", "assets", "Wands", "default", "vr_controller_vive_1_5")

DESTINATION = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "vr_controller_vive_1_5"))

CUSTOM_SENSOR = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "vr_controller_vive_1_5", "custom_sensor"))

def Vive_1_set():

    clear()

    shutil.copytree(SOURCE, DESTINATION, dirs_exist_ok=True)

    if os.path.exists(CUSTOM_SENSOR):
            os.remove(str(CUSTOM_SENSOR))
            
    print("Success")
    input("Press Enter to continue.")