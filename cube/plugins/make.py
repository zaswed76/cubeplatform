import yaml
import paths
import os
from shutil import copy2
from sys import argv

def plugin(name):
    plugins_files = os.listdir(paths.PLUGINS_ABC)
    new_plugin_dir = os.path.join(paths.PLUGINS_FOLDER, name)
    if not  os.path.isdir(new_plugin_dir):
        os.mkdir(new_plugin_dir)
        for f in plugins_files:
            old_path = os.path.join(paths.PLUGINS_ABC, f)
            new_path = os.path.join(new_plugin_dir, f)
            copy2(old_path, new_path)
        edit_manifest(name, paths.PLUGINS_MANIFEST)
        add_css_file(name, paths.BASE_CSS_FOLDER)
        return new_plugin_dir
    else:
        return None

def edit_manifest(plugin_name, manifest_path):
    manifest = load(manifest_path)
    plugins = manifest["plugins"]
    ids = []
    for pl, v in plugins.items():
       ids.append(v["index"])
    last_id = max(ids) if ids else manifest["start_index"]
    next_id = last_id + 1
    plugins[plugin_name] = {"index": next_id}
    save(manifest_path, manifest)

def add_css_file(plugin_name, css_dir):
    css_str = """QFrame#__plugin__{
    background-color: #49d3b8;
}"""
    new_css = css_str.replace("__plugin__", plugin_name)
    new_file = os.path.join(css_dir, "{}.css".format(plugin_name))
    with open(new_file, "w") as somefile:
         somefile.write(new_css)


def load(cfg):
    with open(cfg) as f:
        return yaml.safe_load(f)


def save(cfg, data):
    print(cfg)
    with open(cfg, 'w') as f:
        yaml.dump(data, f)

def main():
    name = argv[1]




if __name__ == '__main__':
    main()
