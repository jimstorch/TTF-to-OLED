from PIL import Image, ImageDraw, ImageFont


TTF_FONT = "NanumGothicCoding-Regular.ttf"
# Tweak this to scale the font to fit the preview
TTF_SIZE=32
# Tweak this to nudge the font up or down in the preview
TTF_DESCENDER = 1

OLED_FONT_WIDTH=16
OLED_FONT_HEIGHT=32
OLED_ROWS = 3
GLYPH_COUNT = 95
FILENAME = "preview.gif"


if __name__ == '__main__':

    font = ImageFont.truetype(TTF_FONT, size=TTF_SIZE)
    image = Image.new("1", (OLED_FONT_WIDTH * GLYPH_COUNT, OLED_FONT_HEIGHT))
    draw = ImageDraw.Draw(image)

    for c in range(GLYPH_COUNT):
        print(chr(c+32))
        draw.text((OLED_FONT_WIDTH * c, 0 - TTF_DESCENDER), chr(c + 32), font=font, fill=1, spacing=None)

    image.save(FILENAME)
    pixels = image.load()

    print(f"const unsigned int font{OLED_FONT_WIDTH}x{OLED_FONT_HEIGHT}[] = {{")

    for c in range(GLYPH_COUNT):
        print("\t", end="");
        for x in range(OLED_FONT_WIDTH):
            segment = 0x00
            mask = 0x01
            for y in range(OLED_FONT_HEIGHT):
                if pixels[x + c * OLED_FONT_WIDTH,y]:
                    segment |= mask
                mask <<= 1
            print(f"0x{segment:08x},", end="")
        if c == 0:
            print(" // <space>" ) 
        elif c == 60:
            # Avoid '\' being read as "line continued" in a source file
            print(" // <backslash>" )   
        else:
            print(" //", chr(c+32))

    print("};")