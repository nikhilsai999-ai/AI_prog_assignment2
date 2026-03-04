import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class CaptchaGenerator:

    def generate_text(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))


class DistortionEngine:

    def create_image(self, text):

        width = 200
        height = 80

        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()

        draw.text((50, 25), text, font=font, fill=(0, 0, 0))

        for _ in range(100):
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.point((x, y), fill=(0, 0, 0))

        image = image.filter(ImageFilter.GaussianBlur(1))

        image.save("captcha.png")

        return image


class CaptchaStorage:

    def __init__(self):
        self.current_captcha = None

    def store(self, text):
        self.current_captcha = text

    def get(self):
        return self.current_captcha


class VerificationSystem:

    def verify(self, user_input, correct_text):
        return user_input == correct_text


class CaptchaSystem:

    def __init__(self):
        self.generator = CaptchaGenerator()
        self.distortion = DistortionEngine()
        self.storage = CaptchaStorage()
        self.verifier = VerificationSystem()

    def run(self):

        print("CAPTCHA Verification System")

        text = self.generator.generate_text()

        self.storage.store(text)

        self.distortion.create_image(text)

        print("CAPTCHA image saved as captcha.png")
        print("Open the image and enter the text.")

        user_input = input("Enter CAPTCHA: ")

        if self.verifier.verify(user_input, self.storage.get()):
            print("Access Granted")
        else:
            print("Access Denied")
            print("Correct CAPTCHA was:", self.storage.get())


system = CaptchaSystem()
system.run()