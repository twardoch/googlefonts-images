# googlefonts-images

CLI tool to render images of each primary font of a font family from [Google Fonts](https://github.com/google/fonts). 

## Installation

Needs macOS. 

1. Install [Homebrew](https://brew.sh/)
2. Install `brew install harfbuzz`
3. Install `brew install python`
4. Install `python3 -m pip install -r requirements.txt`

## Usage

```
usage: build_images [-h] -f folder [-i folder] [-p int]

Takes a folder of Google Fonts and builds images

optional arguments:
  -h, --help            show this help message and exit
  -f folder, --fonts folder
                        Folder with the local copy of https://github.com/google/fonts
  -i folder, --images folder
                        Folder in which the images will be written.
  -p int, --ppm int     PPM size at which the images will be rendered.
```