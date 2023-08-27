from PIL import Image, ImageDraw, ImageFont

def draw(sent_it, sent_en, name, incipit=True):
	base_img = Image.open('scontrino-325x55.jpg')
	im = ImageDraw.Draw(base_img)

	x = 215.4
	font_size = 54

	font = ImageFont.truetype('fonts/PPEditorialNew-Ultralight.ttf', font_size)
	font_italic = ImageFont.truetype('fonts/PPEditorialNew-UltralightItalic.ttf', font_size)

	if incipit:
		im.text((x, 320), sent_it, font=font, fill=(0, 0, 0))
		im.text((x, 410), sent_en, font=font_italic, fill=(0, 0, 0))
	else:
		im.text((x, 566), sent_it, font=font, fill=(0, 0, 0))
		im.text((x, 654), sent_en, font=font_italic, fill=(0, 0, 0))

	#base_img.show()
	base_img.save('images/' + name + '.png')