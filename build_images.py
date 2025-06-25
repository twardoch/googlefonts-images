#!/usr/bin/env python3

import argparse
import random
from collections import OrderedDict
from pathlib import Path

import fontTools.ttLib
import fontTools.unicodedata as ucd
from sh import hb_view as hbv

base_folder = Path(Path(__file__).parent)


class GoogleFontsImageGenerator:
    def __init__(self, fonts_folder, images_folder=None, ppm=17):
        self.ppm = ppm
        self.fonts_folder = Path(fonts_folder)
        if images_folder:
            self.img_base_folder = images_folder
        else:
            self.img_base_folder = Path(base_folder, "img")
        self.fonts = OrderedDict()
        self.fonts_subfolders = ["apache", "ofl", "ufl"]
        self.find_fonts()

    def get_script_unicodes(self, font):
        scripts = OrderedDict()
        scripts_coverage = OrderedDict()
        unicodes = []
        for u in font.getBestCmap().keys():
            if ucd.category(chr(u))[0] not in ("N", "C") and u not in (0xFFFD, 0x0023):
                unicodes.append(u)
                script = ucd.script(chr(u))
                scripts[script] = scripts.get(script, 0) + 1
                scripts_coverage[script] = scripts_coverage.get(script, []) + [u]
        scripts = OrderedDict(sorted(scripts.items(), key=lambda t: t[1], reverse=True))
        for k in ("Zyyy", "Zinh", "Zzzz"):
            if k in scripts.keys():
                del scripts[k]
        scripts = list(scripts.keys()) if len(scripts.keys()) else ["Zsym"]
        return scripts[0], scripts_coverage.get(scripts[0], unicodes)

    def get_script_sample_text_adv(self, font_path, words=5, chars=6):
        font = fontTools.ttLib.TTFont(font_path)
        script, unicodes = self.get_script_unicodes(font)
        cats = OrderedDict()
        for u in unicodes:
            cat = ucd.category(chr(u))[0]
            if cat in "LNS" and ucd.script(chr(u)) == script:
                cats[cat] = cats.get(cat, []) + [u]
        try:
            unicodes = sorted(cats.items(), key=lambda t: len(t[1]), reverse=True)[0][1]
        except:
            unicodes = unicodes
        lensample = words * chars
        if lensample > len(unicodes):
            lensample = len(unicodes)
        sample = "".join([chr(u) for u in random.sample(unicodes, lensample)])
        words = [sample[0 + i : chars + i] for i in range(0, len(sample), chars)]
        newwords = []
        for wordi, word in enumerate(words):
            if int(wordi / len(words) + 0.7):
                newwords.append(word.lower())
            else:
                newwords.append(word.upper())
        return script, newwords

    def find_best_font(self, folder):
        return sorted([str(p) for p in list(Path(folder).glob("**/*.?tf"))], key=len)[0]

    def get_script_sample_text(self, font_path, base):
        script, words = self.get_script_sample_text_adv(font_path)
        if script in ("Latn"):
            words = [base[:6], "RADHES", "Hąmbrg", "geföns"] + [words[-1]]
        return script, " ".join(words)

    def find_fonts(self):
        for fonts_subfolder in self.fonts_subfolders:
            fonts_subfolder = Path(self.fonts_folder, fonts_subfolder)
            for folder in sorted(list(fonts_subfolder.iterdir())):
                if folder.is_dir():
                    self.fonts[str(Path(folder).stem)] = self.find_best_font(folder)

    def render_font(self, font_path, png_path, text, ppm=None, script="Latn"):
        if not ppm:
            ppm = self.ppm
        hbv(
            font_file=font_path,
            font_size=ppm,
            font_ppem=ppm,
            text=text,
            script=script,
            margin=2,
            output_format="png",
            output_file=png_path,
        )

    def render_fonts(self):
        png_folder = Path(self.img_base_folder, str(self.ppm))
        if not png_folder.is_dir():
            png_folder.mkdir(parents=True)
        for base in list(self.fonts.keys()):
            font_path = self.fonts[base]
            png_path = Path(png_folder, base + ".png")
            script, sample_text = self.get_script_sample_text(font_path, base)
            self.render_font(font_path, png_path, sample_text, self.ppm, script)
            print(base, script, sample_text, font_path)


def cli():
    parser = argparse.ArgumentParser(
        prog="./build_images.py",
        description="""Takes a folder of Google Fonts and builds images""",
    )
    parser.add_argument(
        "-f",
        "--fonts",
        required=True,
        metavar="folder",
        dest="fonts_folder",
        help="""Folder with the local copy of https://github.com/google/fonts""",
    )
    parser.add_argument(
        "-i",
        "--images",
        required=False,
        metavar="folder",
        dest="images_folder",
        help="Folder in which the images will be written.",
    )
    parser.add_argument(
        "-p",
        "--ppm",
        default=17,
        required=False,
        type=int,
        metavar="int",
        dest="ppm",
        help="PPM size at which the images will be rendered.",
    )

    args = parser.parse_args()
    print("Running with %s" % (repr(vars(args))))

    gfig = GoogleFontsImageGenerator(
        fonts_folder=args.fonts_folder, images_folder=args.images_folder, ppm=args.ppm
    )
    gfig.render_fonts()


if __name__ == "__main__":
    cli()
