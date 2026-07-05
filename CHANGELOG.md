# Changelog

All notable changes to this project are documented here. Versions follow the git tags (`vX.Y.Z`).

## [Unreleased]

### Changed
- Rewrote `README.md` to explain what the image gallery is, the guessable URL schema, how each thumbnail is chosen and rendered, and how to regenerate the set locally.

### Added
- `docs/assets/icon.png` — a single-line concept illustration (a camera photographing a framed "font portrait").
- `.gitignore` entries for `.DS_Store` and Jekyll build artifacts (`_site/`, `.jekyll-cache/`, `.jekyll-metadata`).

### Removed
- Stopped tracking `.DS_Store`.

## [1.0.1]
- Prior tagged release. Full image set (~1,380 family thumbnails at 17 PPM) and the `build_images.py` render script.
