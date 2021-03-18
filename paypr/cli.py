""" CLI for Paypr """

import click
from paypr import Paypr


@click.command()
@click.option(
    "--input",
    "-i",
    required=True,
    prompt="Input file name",
    help="The input file, must be an image.",
)
@click.option(
    "--size",
    "-s",
    default="FHD",
    prompt="Output file size",
    help="The output size for the wallpaper. Format options are HD, FHD, WUXGA, QHD, 2K, UHD, 4K, and 5K",
    type=click.Choice(
        ["HD", "FHD", "WUXGA", "QHD", "2K", "UHD", "4K", "5K"], case_sensitive=False
    ),
)
def main(input, size):
    wallpaper = Paypr(input_image=input, output_size=size.upper())
    wallpaper.create_wallpaper()