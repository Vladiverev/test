from PIL import ImageGrab
screen = ImageGrab.grab()
screen.save('./data/screenshot.png', 'PNG')
