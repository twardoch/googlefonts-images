# googlefonts-images

CLI tool to render images of each primary font of a font family from [Google Fonts](https://github.com/google/fonts).

1. The tool uses the `hb-view` CLI tool to render samples at the desired PPM.
2. The tool creates sample text randomly for non-Latin fonts (using the dominant script of the font, determined by the largest codepoint coverage), and for fonts that support the Latin script, it uses a predefined sample text plus one randomly-generated word. For non-Latin fonts, the samples may be nonsensical and produce odd character combinations for connecting scripts.
3. The PNG images are accessible via URL like `https://twardoch.github.io/googlefonts-images/img/17/roboto.png`
4. Each image base name corresponds to the folder name of the family in the Google Fonts repo, like `https://github.com/google/fonts/tree/main/apache/roboto` in the above example.
5. Only the "main" font from each family folder is rendered. The "main" font gets determined by its shortest path name.


## Installation

Needs macOS, perhaps also works on Linux.

1. Install [Homebrew](https://brew.sh/) on macOS.
2. Run `brew install harfbuzz` or install `harfbuzz` on Linux.
3. Run `brew install python` or install Python 3.9 or newer on Linux.
4. Run `python3 -m pip install -r requirements.txt`

## Usage

```
usage: ./build_images.py [-h] -f folder [-i folder] [-p int]

Takes a folder of Google Fonts and builds images

optional arguments:
  -h, --help            show this help message and exit
  -f folder, --fonts folder
                        Folder with the local copy of https://github.com/google/fonts
  -i folder, --images folder
                        Folder in which the images will be written.
  -p int, --ppm int     PPM size at which the images will be rendered.
```

