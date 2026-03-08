from pathlib import Path
import sys

from PIL import Image, ImageDraw


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: make_icon.py OUTPUT_PATH")
        return 1

    output_path = Path(sys.argv[1])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    size = 256
    image = Image.new("RGBA", (size, size), "#f3b6c3")
    draw = ImageDraw.Draw(image)

    blue = "#2d3eff"
    dark = "#1f1f1f"
    white = "#ffffff"
    red = "#d62839"

    draw.rounded_rectangle((12, 12, 244, 244), radius=28, outline=dark, width=6, fill="#edb2c0")
    draw.line((128, 28, 128, 228), fill=dark, width=4)
    draw.ellipse((112, 112, 144, 144), outline=dark, width=4)
    draw.rectangle((28, 84, 42, 172), fill=blue)
    draw.rectangle((214, 84, 228, 172), fill=blue)
    draw.ellipse((170, 110, 190, 130), fill=blue)
    draw.rectangle((84, 26, 172, 44), fill=white)
    draw.text((96, 27), "PONG", fill=red)

    image.save(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
