# googlefonts-images

CLI tool to render images of each primary font of a font family from [Google Fonts](https://github.com/google/fonts).

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

## Result

1. The PNG images are accessible via URL like `https://twardoch.github.io/googlefonts-images/img/17/roboto.png`
2. Each image base name corresponds to the folder name of the family in the Google Fonts repo, like `https://github.com/google/fonts/tree/main/apache/roboto` in the above example.
3. Only the "main" font from each family folder is rendered. The "main" font gets determined by its shortest path name.

