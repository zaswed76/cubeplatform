import os
from pathlib import Path

ROOT = os.path.dirname(__file__)
# ROOT = Path.cwd()


MAIN_CONFIG = os.path.join(ROOT, "settings/main_config.yaml")
CSS_FOLDER = os.path.join(ROOT, "css")
BASE_CSS_FOLDER = os.path.join(ROOT, "css", "base")

PLUGINS_FOLDER = os.path.join(ROOT, "plugins")
PLUGINS_ABC = os.path.join(ROOT, "plugins", "resource/baseGame")
PLUGINS_MANIFEST = os.path.join(ROOT, "plugins", "manifest.yaml")

DOC_FOLDER = Path(ROOT).parent
DOC_INDEX = os.path.join(DOC_FOLDER, "doc/build/html/index.html")
GAME_RESOURCES = os.path.join(ROOT, "resource/gameresource")
print(GAME_RESOURCES)


def get_res_folder(*args):
    return os.path.join(GAME_RESOURCES, *args)

"/home/sergdell/pyprojects/pyprojects/cubeplatform/cube/resource/"

if __name__ == '__main__':
    print(get_res_folder("cubeSerg", "images"))


