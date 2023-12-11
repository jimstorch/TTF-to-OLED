# TTF to OLED

I needed some larger monospaced fonts for using those tiny OLED display modules
driven by SSD1306 or SSD1306 ICs.

This script is not clever.  It prints a horizontal line of MONOSPACE characters
from ' ' (ASCII Space) to '~' to a file named 'preview.gif' and scans the
resulting image into bit data.  It dumps out to the console for copy/pasting
or 
```
python3 ttf_to_oled >> my_font.h
``````

Play with the TTF_SIZE and TTF_DESCENDER to get your font scaled/vertical
aligned.

Edit line 41 if you don't need the full 32bit hex and want to save horizontal
source code, e.g.:

```python
print(f"0x{segment:08x},", end="")  # 0x00000000
print(f"0x{segment:06x},", end="")  # 0x000000
print(f"0x{segment:04x},", end="")  # 0x0000
print(f"0x{segment:08x},", end="")  # 0x00 (can change the array to 'unsigned char') 
```

## Requirements
* https://pypi.org/project/Pillow/

```sh
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

