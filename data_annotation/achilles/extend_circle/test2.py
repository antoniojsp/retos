from PIL import Image
import numpy as np


def process_image(image):
    """Removes the black frame from an image and stretches the content.

    Args:
        image: A 2D array (list of lists) representing the image.
               Each pixel is a tuple of three integers (R, G, B).

    Returns:
        A new 2D array with the same dimensions as the input,
        where the black frame has been removed and the content stretched.
    """
    # Convert the input to a numpy array
    img_array = np.array(image, dtype=np.uint8)

    # Find the boundaries of the non-black content
    rows, cols = np.where(np.any(img_array != 0, axis=2))
    top, bottom = rows.min(), rows.max()
    left, right = cols.min(), cols.max()

    # Extract the content without the black frame
    content = img_array[top:bottom + 1, left:right + 1]

    # Create a PIL Image from the content
    pil_image = Image.fromarray(content)

    # Resize the image back to original dimensions
    original_size = img_array.shape[:2]
    resized_image = pil_image.resize(original_size[::-1], Image.LANCZOS)

    # Convert back to numpy array
    result = np.array(resized_image)

    return result.tolist()


# Example usage:
image = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
]

result = process_image(image)

# Print the result
for row in result:
    print(row)
