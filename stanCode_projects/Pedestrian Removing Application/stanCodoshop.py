"""
SC101_Assignment3
Adapted from Nick Parlante's Ghost assignment by Jerry Liao.
-------------------
File: stanCodoshop.py
Name: Yuzu
Description: I have written a photoshop code!
-------------------
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    return ((pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2) ** (1 / 2)


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r, g, b = 0, 0, 0
    n = len(pixels)
    for p in pixels:
        r += p.red
        g += p.green
        b += p.blue
    return [r // n, g // n, b // n]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # r, g, b = get_average(pixels)
    # dist = []
    # #distance list
    # for p in pixels:
    #     k = get_pixel_dist(p, r, g, b)
    #     dist.append(k)
    # d = float("inf")
    # #find minimum of distance list
    # for s in dist:
    #     if s < d:
    #         d = s
    # #find the pixel
    # for p in pixels:
    #     if d == get_pixel_dist(p, r, g, b):
    #         return p

    r, g, b = get_average(pixels)
    d = [get_pixel_dist(p, r, g, b) for p in pixels]
    return pixels[d.index(min(d))]

    # a = list(get_pixel_dist(pixels[i], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2]) for i in
    #          range(len(pixels)))
    # return pixels[a.index(min(a))]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for i in range(width):
        for j in range(height):
            pixels = list(image.get_pixel(i, j) for image in images)
            result.set_pixel(i, j, get_best_pixel(pixels))
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
