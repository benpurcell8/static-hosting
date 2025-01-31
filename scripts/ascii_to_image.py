from PIL import Image, ImageDraw, ImageFont

# ASCII art
ascii_art = """
(\(\\
(-.-)
o_(")(")
"""

# Create a new image with a larger size
image = Image.new('RGB', (300, 150), color='white')
draw = ImageDraw.Draw(image)

# Load a larger font
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 20)

# Draw the ASCII art on the image
draw.text((10, 10), ascii_art, font=font, fill='black')

# Save the image
image.save('assets/rabbit.png') 