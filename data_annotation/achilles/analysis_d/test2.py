import gradio as gr
from colorthief import ColorThief
import requests
from io import BytesIO
from PIL import Image
import random


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def process_image(image_url: str) -> list:
    """Processes an image from a URL and extracts 7 color palettes.

    Fetches an image from the provided URL, processes it to extract dominant colors,
    and generates 7 distinct color palettes. Each palette is a list of hex color codes.

    Args:
      image_url: The URL of the image to process.

    Returns:
      A list of 7 color palettes. Each palette is a list of hex color codes
      (e.g., ["#FFFFFF", "#000000", "#FF0000"]).
    """
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Save to a temporary file
    temp_file = BytesIO()
    img.save(temp_file, format='PNG')
    temp_file.seek(0)

    # Use ColorThief to extract colors
    color_thief = ColorThief(temp_file)

    palettes = []
    for _ in range(7):
        palette = color_thief.get_palette(color_count=5)
        hex_palette = [rgb_to_hex(color) for color in palette]
        palettes.append(hex_palette)

    return palettes


def display_palettes(image_url):
    image = Image.open(requests.get(image_url, stream=True).raw)
    palettes = process_image(image_url)

    # Create color swatches for each palette
    palette_images = []
    for palette in palettes:
        swatch = Image.new('RGB', (500, 100))
        for i, color in enumerate(palette):
            draw = Image.new('RGB', (100, 100), color)
            swatch.paste(draw, (i * 100, 0))
        palette_images.append(swatch)

    return image, palette_images


# Define image URLs
image_urls = [
    "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png",
    "https://www.gstatic.com/webp/gallery3/1.png"
]

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Color Palette Generator")
    with gr.Row():
        image_dropdown = gr.Dropdown(choices=image_urls, label="Select an image")
    with gr.Row():
        image_output = gr.Image(label="Selected Image")
    with gr.Row():
        gallery_output = gr.Gallery(label="Color Palettes", show_label=True, elem_id="gallery").style(grid=2,
                                                                                                      height="auto")

    image_dropdown.change(fn=display_palettes, inputs=image_dropdown, outputs=[image_output, gallery_output])

demo.launch()