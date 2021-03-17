#! Python 3.9
# This application will take in an image and
#  an output screen size (1080p, 2k, 4k, etc.)
#  and output the image resized to best fit
#  the screen with a blown up, blurred out
#  version of the same image behind it.
from PIL import Image, ImageFilter
import sys
from datetime import date

# Constant screen size tuples
SS_HD = (1280, 720)
SS_FHD = (1920, 1080)
SS_WUXGA = (1920, 1200)
SS_QHD, SS_2K = (2560, 1440)
SS_UHD, SS_4K = (3840, 2160)
SS_5K = (5120, 2880)

SCREEN_SIZES = {
    "HD": SS_HD,
    "FHD": SS_FHD,
    "WUXGA": SS_WUXGA,
    "QHD": SS_QHD,
    "2K": SS_2K,
    "UHD": SS_UHD,
    "4K": SS_4K,
    "5K": SS_5K,
}

# Orientations
O_PORTRAIT = "portrait"
O_LANDSCAPE = "landscape"
O_SQUARE = "square"


class Paypr:
    def __init__(self, input_image, output_size="FHD"):
        self.input_image = Image.open(input_image)
        self.input_image_width, self.input_image_height = self.input_image.size
        self.input_orientation = self._set_orientation(
            self.input_image_width, self.input_image_height
        )
        self.output_size = SCREEN_SIZES[output_size]
        self.output_image_name = f"{input_image}_{date.today()}.png"
        self.output_image = Image.new("RGBA", self.output_size)

    def _set_orientation(self, width, height):
        if width > height:
            return O_LANDSCAPE
        elif height > width:
            return O_PORTRAIT
        else:
            return O_SQUARE

    # Setting input image larger than output size and blurring
    def _output_image_background(self):
        bg_width = 0
        bg_height = 0
        crop_box_x_front = 0
        crop_box_x_back = 0
        crop_box_y_front = 0
        crop_box_y_back = 0

        if self.input_orientation == O_SQUARE or self.input_orientation == O_PORTRAIT:
            bg_width = self.output_size[0] + 10
            bg_height = int(
                (float(bg_width) / float(self.input_image_width))
                * float(self.input_image_height)
            )
            bg_middpoint = (int(bg_width / 2), int(bg_height / 2))
            crop_box_x_front = 5
            crop_box_x_back = self.output_size[0] - 4
            crop_box_y_front = bg_middpoint[1] - int(self.output_size[1] / 2)
            crop_box_y_back = crop_box_y_front + self.output_size[1]
        else:
            bg_height = self.output_size[1] + 10
            bg_width = int(
                (float(bg_height) / float(self.input_image_height))
                * float(self.input_image_width)
            )
            bg_middpoint = (int(bg_width / 2), int(bg_height / 2))
            crop_box_y_front = 5
            crop_box_y_back = self.output_size[1] - 4
            crop_box_x_front = bg_middpoint[0] - int(self.output_size[0] / 2)
            crop_box_x_back = crop_box_x_front + self.output_size[0]

        # print(
        #     f"Resizing to: width:{bg_width} height:{bg_height} from {self.input_image.size}"
        # )
        # print(
        #     f"Cropping to {crop_box_x_front}, {crop_box_y_front}, {crop_box_x_back}, {crop_box_y_back}"
        # )

        bg_image = (
            self.input_image.resize((bg_width, bg_height))
            .filter(filter=ImageFilter.GaussianBlur(20))
            .crop(
                (crop_box_x_front, crop_box_y_front, crop_box_x_back, crop_box_y_back)
            )
        )
        self.output_image.paste(bg_image)

    def _output_image_foreground(self):
        leading_x = 0
        leading_y = 0
        # TODO: Calculate the top left corner of the image
        self.output_image.paste(self.input_image, (leading_x, leading_y))

    # Main entry point for application
    def create_wallpaper(self):
        print("Creating Wallpaper...")
        self._output_image_background()
        self._output_image_foreground()

        self.output_image.save(self.output_image_name)


if __name__ == "__main__":
    wallpaper = Paypr(input_image="398027.jpg")
    wallpaper.create_wallpaper()