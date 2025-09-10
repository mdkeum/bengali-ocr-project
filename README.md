# Bengali OCR Benchmark

This project benchmarks Tesseract OCR and EasyOCR on a diverse set of Bengali documents. It evaluates accuracy and speed using 216 images across 9 categories, with a custom preprocessing pipeline to improve results. The study highlights strengths and weaknesses of each OCR engine for Bengali text recognition.

## Setup

- Developed and tested in Google Colab.
- Requires Python packages: `easyocr`, `opencv-python-headless`.

## Usage

1. Mount your Google Drive with dataset.
2. Update the `base_path` variable to point to your dataset location.
3. Run the notebook/script to perform OCR and save text outputs.

## Notes

- GPU acceleration is recommended for faster OCR processing.
- Dataset is not included due to size/privacy.
