import numpy as np

import numpy as np


def contraharmonic_filter(image, size, Q):
    """
    Applies a contraharmonic mean filter to an input image.

    Args:
        image: A 2D numpy array representing a grayscale image.
        size: An integer representing the size of the filter window (e.g., 3 for a 3x3 window).
        Q: A float representing the order of the contraharmonic mean filter.

    Returns:
        A 2D numpy array representing the filtered image.
    """

    pad_size = size // 2
    padded_image = np.pad(image, pad_size, mode='reflect')
    print(padded_image)

    output_image = np.zeros_like(image)
    # print(output_image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + size, j:j + size]
            print(np.power(window, Q + 1))
            numerator = np.sum(np.power(window, Q + 1))
            print(numerator)
            denominator = np.sum(np.power(window, Q))
            print(denominator)

            if denominator == 0:
                if numerator == 0:
                    output_image[i, j] = 0
                else:
                    output_image[i, j] = np.mean(window)
            else:
                output_image[i, j] = numerator / denominator

    return output_image


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