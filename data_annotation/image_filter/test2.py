import numpy as np


def contraharmonic_filter(image, size, Q):
    """
    Apply a contraharmonic mean filter to a grayscale image.

    Parameters:
    - image: 2D numpy array representing a grayscale image.
    - size: integer representing the size of the filter window (e.g., 3 for a 3x3 window).
    - Q: float representing the order of the contraharmonic mean filter.

    Returns:
    - Filtered image as a 2D numpy array.
    """
    # Padding width
    pad_width = size // 2

    # Pad the image with edge values
    padded_image = np.pad(image, pad_width, mode='edge')
    print(padded_image)
    # Prepare an output image
    filtered_image = np.zeros_like(image, dtype=np.float64)

    # Iterate over each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Get the window from the padded image
            window = padded_image[i:i + size, j:j + size]
            print(window ** (Q + 1), "\n")
            # Calculate the numerator and denominator

            numerator = np.sum(window ** (Q + 1))
            print(numerator)
            denominator = np.sum(window ** Q)
            print(denominator)
            print()
            if denominator == 0:
                if numerator == 0:
                    filtered_image[i, j] = 0  # Both numerator and denominator are zero
                else:
                    filtered_image[i, j] = np.mean(window)  # Avoid division by zero
            else:
                filtered_image[i, j] = numerator / denominator

    return filtered_image


# Example usage
if __name__ == "__main__":
    # Create a sample image (grayscale)
    sample_image = np.array([
        [10, 10, 10, 10],
        [10, 10, 50, 50],
        [10, 10, 50, 50],
        [10, 10, 10, 10]
    ], dtype=np.float64)

    # Apply the contraharmonic filter with a 3x3 window and Q = 1.5
    filtered_image = contraharmonic_filter(sample_image, size=3, Q=1.5)
    print(filtered_image)