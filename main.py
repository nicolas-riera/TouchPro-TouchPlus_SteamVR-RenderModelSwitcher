from src.action_selector import action_selector
from src.get_SteamVR_path import get_SteamVR_path

def main():
    get_SteamVR_path()
    action_selector()

if __name__ == "__main__":
    main()