""" CLI for Paypr """

import click
from paypr import Paypr


@click.command()
@click.option("--input", "-i", prompt="Input file name")
@click.option(
    "--size",
    "-s",
    default="FHD",
    prompt="Output file size",
    help="The output size for the wallpaper. Format options are HD, FHD, WUXGA, QHD, 2K, UHD, 4K, and 5K",
)
def main(input, size):
    wallpaper = Paypr(input_image=input, output_size=size)
    wallpaper.create_wallpaper()