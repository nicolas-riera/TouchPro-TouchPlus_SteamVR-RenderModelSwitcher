import os

from src.get_SteamVR_path import real_case_path, find_steam_path

def check_current_rendermodel():
    
    if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_left", "oculus_quest_plus_controller_left.obj")):
        return "Touch Plus"
    elif os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_left", "oculus_quest_pro_controller_left.obj")):
        return "Touch Pro"
    else:
        return "Unknown"
