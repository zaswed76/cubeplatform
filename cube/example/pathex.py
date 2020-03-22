
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paths

from pathlib import Path
Path()

img_dir = Path(paths.ROOT) / "resource" / "gameresource"/ "cubeSerg" / "images"

print(img_dir)
print(img_dir.is_dir())
for p in img_dir.rglob("*.png"):
    print(p)


