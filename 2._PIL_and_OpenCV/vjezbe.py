from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import os


meme = r"C:\Users\user\Downloads/20201215_1402550.jpg"


def zad1():
  data = r"2._PIL_and_OpenCV\materials\auto.jpg"
  image = Image.open(data)

  image.show()

  del image


def zad2():
  data = r"2._PIL_and_OpenCV\materials\pillow_logo.png"
  image = Image.open(data)

  # Format
  print("Format:", image.format)
  # Dimensions in pixels
  print("Pixels:", image.size)
  # Height in pixels
  print("Height:", image.height)
  # Color mode
  print("Color mode:", image.mode)

  del image


def zad3():
  data = r"2._PIL_and_OpenCV\materials\auto.jpg"
  image = Image.open(data)

  # Grayscale conversion
  im_gray = image.convert("L")

  # a) Turning into Numpy array
  a = np.asarray(im_gray)
  print("Array:", a)
  
  # b) Arra data
  print("Width:", len(a[0]))
  print("Height:", len(a))
  # temporary wrong solution
  print("Number of channels:", int(len(a[0])/im_gray.width))

  # c)
  im_gray.show()

  # d) 1-bit conversion
  im_1bit = image.convert("1")
  im_1bit.show()

  # e) Concatenate / combine two images horizontally
  dst = Image.new('RGB', (image.width + im_gray.width, image.height))
  dst.paste(image, (0, 0))
  dst.paste(im_gray, (image.width, 0))
  dst.show()

  del image


def zad4():
  data = r"2._PIL_and_OpenCV\materials\pillow_logo.png"
  image = Image.open(data)

  im_gray = image.convert("L")

  im_gray.save("2._PIL_and_OpenCV\output\pillow_logo_grayscale.png")

  im_alpha = im_gray.copy()
  im_alpha.putalpha(256)
  im_alpha.save("2._PIL_and_OpenCV\output\pillow_logo_grayscale_alpha.png")

  # The size of the file increased.


def zad5():
  directory = r"2._PIL_and_OpenCV\materials\animals"
  output_dir = r"2._PIL_and_OpenCV\output\PNGS\\"

  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
      image = Image.open(f)
      image.save(output_dir + filename[:len(filename)-4] + ".png", "PNG")
      del image
    f.close()


def zad6():
  data = r"2._PIL_and_OpenCV\materials\animals\lav.jpg"
  image = Image.open(data)

  # a) Rotated by 45 degrees
  image.rotate(45).show()

  # b) Flip vertically
  vertical = image.transpose(Image.FLIP_LEFT_RIGHT)
  vertical.show()

  # c) Saved previous image as PDF
  vertical.save("2._PIL_and_OpenCV\output\lav.pdf", "PDF")


def zad7():
  data = r"2._PIL_and_OpenCV\materials\animals\paun.jpg"
  image = Image.open(data)

  a = image.filter(ImageFilter.GaussianBlur(35))
  b = image.filter(ImageFilter.CONTOUR)
  c = image.filter(ImageFilter.EMBOSS)
  d = image.filter(ImageFilter.UnsharpMask(85, 350, 55))
  e = image.filter(ImageFilter.MedianFilter(15))

  arr = [a, b, c, d, e]
  arr2 = "abcde"

  # create figure
  fig = plt.figure(figsize=(10, 7))
    
  # setting values to rows and column variables
  rows = 2
  columns = 3

  # Adds a subplot at the 1st position
  fig.add_subplot(rows, columns, 1)
  plt.imshow(image)
  plt.axis('off')
  plt.title("Initial")

  for i in range(len(arr)):
    fig.add_subplot(rows, columns, i+2)
    plt.imshow(arr[i])
    plt.axis('off')
    plt.title(arr2[i])

  plt.show()
  


def zad8():
  data = r"2._PIL_and_OpenCV\materials\animals\orca.jpg"
  image = Image.open(data)

  # def contrast(c):
  #   if c > 128:
  #     return int(c*1.35)
  #   else:
  #     return int(c*0.65)

  enhanced = image.point(lambda i: i*1.35)

  enhanced.show()


zad8()


