import gradio as gr
from PIL import Image
import requests
from io import BytesIO
from colorthief import ColorThief

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

  color_thief = ColorThief(BytesIO(response.content))

  # Get color palettes of different sizes
  palettes = []
  for n in [3, 5, 7, 9, 12, 15, 20]:
      palette = color_thief.get_palette(color_count=n)
      hex_palette = ["#" + "".join("%02x" % c for c in color) for color in palette]
      palettes.append(hex_palette)

  return palettes

  image_urls = [
      "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif",
      "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png",
      "https://www.gstatic.com/webp/gallery3/1.png"
  ]

  with gr.Blocks() as demo:
      with gr.Row():
          image_input = gr.Dropdown(choices=image_urls, label="Select an Image")
          image_output = gr.Image(label="Selected Image")
      with gr.Row():
          button = gr.Button("Generate Color Palettes")
      with gr.Row():
          gallery = gr.Gallery(label="Color Palettes").style(grid=[1, 7])

      def on_image_change(image_url):
          response = requests.get(image_url)
          return Image.open(BytesIO(response.content))

      image_input.change(fn=on_image_change, inputs=image_input, outputs=image_output)

      button.click(fn=process_image, inputs=image_input, outputs=gallery)

      demo.launch()
