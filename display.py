from PIL import Image, ImageOps

try:
    from inky.inky_uc8159 import Inky
except Exception:

    class Inky:
        def set_image(*args, **kwargs):
            print("set!")

        def show(self):
            print("show!")


class Display:
    def __init__(self, saturation=0.5):
        self.inky = Inky()
        self.saturation = saturation

    def resize_for_screen(self, image):
        copied = image.copy()

        # Apply rotation in exif data
        copied = ImageOps.exif_transpose(image)

        copied.thumbnail([600, 448])
        size = copied.size
        print(size)
        background = Image.new("RGB", (600, 448), (255, 255, 255))
        background.paste(copied, (int((600 - size[0]) / 2), int((448 - size[1]) / 2)))
        return background

    def show_latest(self):
        latest_image = self.resize_for_screen(Image.open("latest"))

        self.inky.set_image(latest_image, saturation=self.saturation)
        self.inky.show(busy_wait=False)
