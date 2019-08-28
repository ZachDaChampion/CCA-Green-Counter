from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


count = 0

sq_feet_per_pixel = 26.165965

# load image
# image_raw = Image.open('top_view.jpg')
image_raw = Image.open('cropped.png')
image_raw = image_raw.convert('RGB')
image = image_raw.load()


# calculate green-ness
green = (0, 255, 0)
def greenness(pixel, reference=green):
  return ((reference[0] - pixel[0]) ** 2 + (reference[1] - pixel[1]) ** 2 + (reference[2] - pixel[2]) ** 2) ** .5


# calculate grassiness
def grassiness(pixel):
  score = min(greenness(image[pixel[0], pixel[1]]), greenness(image[pixel[0], pixel[1]], reference=(30, 50, 30)) * 1.5, greenness(image[pixel[0], pixel[1]], reference=(130, 130, 100)) * 3)

  neighbor_bias = .5
  if pixel[0] > 0: score += greenness(image[pixel[0] - 1, pixel[1]]) * neighbor_bias
  if pixel[0] < width - 1: score += greenness(image[pixel[0] + 1, pixel[1]]) * neighbor_bias
  if pixel[1] > 0: score += greenness(image[pixel[0], pixel[1] - 1]) * neighbor_bias
  if pixel[1] < height - 1: score += greenness(image[pixel[0], pixel[1] + 1]) * neighbor_bias
    
  return score



# loop through pixels
width = image_raw.width
height = image_raw.height
for x in range(width):
  for y in range(height):
    if grassiness((x, y)) > 535:
      image[x, y] = (image[x, y][0] - 125, image[x, y][1] - 200, image[x, y][2] - 125)
    else:
      image[x, y] = (image[x, y][0] + 0, image[x, y][1] + 50, image[x, y][2] + 0)
      count += 1


# show image
imgplot = plt.imshow(image_raw)
print(count * sq_feet_per_pixel)
plt.show() 