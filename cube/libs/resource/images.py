from pathlib import Path

_EXTS = (".png", ".jpg", ".PNG", ".JPG", ".jpeg")

class ImagesObject:
    def __init__(self, folder, *exts):
        self.folder = folder
        self._pathObj = Path(self.folder)
        self._images = []
        self.exts = exts
        if not self.exts:
            self.exts = _EXTS
        self.reload_images()

    def images(self):
        return self._images

    def sortImages(self, reverse=False):
        return sorted(self._images, reverse=reverse)

    def reload_images(self):
        self._images.clear()
        for e in self.exts:
            self._images.extend([str(x) for x in self._pathObj.glob(f"*{e}")])

    def segmentImages(self, start, end):
        return [x for x in range(start, end+1)]

    def setExt(self, *exts):
        self.exts = exts
        self.reload_images()


    def __repr__(self):
        return "work dir - {}".format(self.folder)

if __name__ == '__main__':
    import paths
    import pprint
    image_folder = paths.get_res_folder("cubeSerg", "test")
    img_obj = ImagesObject(image_folder, ".png")
    # pprint.pprint(img_obj.images())
    pprint.pprint(img_obj.sortImages(reverse=True))
    pprint.pprint(img_obj.segmentImages(0, 9))