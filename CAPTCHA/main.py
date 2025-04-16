# importing the important libraries

import random
import string
from PIL import Image
import os
from captcha.image import ImageCaptcha


# Generate a random CAPTCHA text with uppercase letters and digits
def generate_captcha_text():
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choices(characters, k=8))


captcha_txt = generate_captcha_text()


# Get the user input and verify it with the CAPTCHA text
def input_verification():
    # Get user input
    user_input = input("Enter the CAPTCHA text you see in the image: ").strip().upper()

    # Verify the user input with captcha_txt
    if user_input == captcha_txt:
        print("CAPTCHA verification passed!")
    else:
        print(f"CAPTCHA verification failed! The correct text was: {captcha_txt}")


def main():
    # Generate CAPTCHA image

    image = ImageCaptcha(width=400, height=220 , fonts=['arial.ttf', 'times.ttf'],font_sizes=(40, 70, 100))
    image.write(captcha_txt, "CAPTCHA.png")

    # Save the CAPTCHA image
    img = Image.open('CAPTCHA.png')  # Load the image
    img.save('CAPTCHA.png')  # Save the image

    # Display the CAPTCHA image
    os.startfile("CAPTCHA.png")

    # Get the verification function
    input_verification()


if __name__ == "__main__":
    main()
