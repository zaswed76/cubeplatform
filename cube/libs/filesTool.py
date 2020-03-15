import fileinput
import glob


def fileInput(folder):
    files_list = glob.glob(folder+"/*.css")
    ls = []
    with fileinput.input(files=files_list) as f:
        for line in f:
            ls.append(line)
    return "".join(ls)