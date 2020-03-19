

import webbrowser

import os
try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x

url = 'file:{}'.format(pathname2url(os.path.abspath('/home/sergdell/pyprojects/pyprojects/cubeplatform/doc/build/html/index.html')))
webbrowser.open(url)

