import os
import winreg
import time
from pathlib import Path

def find_steam_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
        steam_path, _ = winreg.QueryValueEx(key, "SteamPath")
        return steam_path
    except FileNotFoundError:
        return None

def real_case_path(path):
    p = Path(path)
    parts = []
    while p != p.parent:
        parent = p.parent
        for child in os.listdir(parent):
            if child.lower() == p.name.lower():
                parts.insert(0, child)
                break
        p = parent
    parts.insert(0, p.drive.capitalize()) 
    parts.insert(1, "\\") 
    return os.path.join(*parts)
    
def find_steamvr_path():
    steam_path = find_steam_path()
    if steam_path:
        steamvr_path = os.path.join(steam_path, "steamapps", "common", "SteamVR")
        if os.path.exists(steamvr_path):
            return steamvr_path
    return None

def get_SteamVR_path():
    if find_steam_path():
        pass
    else:
        print("SteamVR Not Found. Program will exit.")
        time.sleep(3)
        exit()
