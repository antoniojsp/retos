from PIL import Image


def process_image(image):
  """Removes the black frame from an image and stretches the content.

  Args:
    image: A 2D array (list of lists) representing the image.
           Each pixel is a tuple of three integers (R, G, B).

  Returns:
    A new 2D array with the same dimensions as the input,
    where the black frame has been removed and the content stretched.
  """
  height = len(image)
  width = len(image[0])
  # Find the boundaries of the non-black content
  top, bottom, left, right = height, 0, width, 0
  for y in range(height):
    for x in range(width):
      if image[y][x] != (0, 0, 0):
          top = min(top, y)
          bottom = max(bottom, y)
          left = min(left, x)
          right = max(right, x)

          # Create a new image with the content only
      content = [row[left:right + 1] for row in image[top:bottom + 1]]

      # Create a PIL Image from the content
      content_image = Image.new("RGB", (right - left + 1, bottom - top + 1))
      content_image.putdata([pixel for row in content for pixel in row])

      # Resize the content image back to the original dimensions
      resized_image = content_image.resize((width, height))

      # Convert the resized image back to a 2D array
      processed_image = [
          list(resized_image.getpixel((x, y))) for y in range(height) for x in range(width)
      ]

      # Reshape the processed image into the correct 2D format
      processed_image = [processed_image[i:i + width] for i in range(0, len(processed_image), width)]
      return processed_image


image = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
]

processed_image = process_image(image)
print(processed_image)