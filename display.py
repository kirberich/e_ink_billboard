from PIL import Image, ImageOps
import threading

try:
    from inky.inky_uc8159 import Inky
except Exception:

    class Inky:
        def set_image(self, *args, **kwargs):
            print("set!")

        def show(self, *args, **kwargs):
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

    def _show_latest(self):
        latest_image = self.resize_for_screen(Image.open("latest"))

        self.inky.set_image(latest_image, saturation=self.saturation)
        self.inky.show(busy_wait=False)
        print("done")

    def show_latest(self):
        task = threading.Thread(target=self._show_latest, args=())
        task.start()
