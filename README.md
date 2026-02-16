# JPG to PNG Converter

A Python-based image conversion utility built with the Pillow library.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Project Summary

This project demonstrates practical experience working with:

- Third-party libraries (Pillow)
- File handling and image processing
- Modular function design
- Command-line execution
- Clean, readable Python code

The tool converts JPG/JPEG images into PNG format while maintaining image fidelity.

## Technical Stack

- Python 3
- Pillow (PIL fork)

## Key Implementation Details

- Uses context managers for safe file handling
- Converts images to RGB to ensure compatibility
- Designed for extensibility (batch processing ready)
- Clean separation of conversion logic

Core Function:
```Python
from PIL import Image

def convert_jpg_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "PNG")
```
## Why This Project Matters

Image processing is a foundational skill for many domains including:

- Backend development
- Automation
- Data pipelines
- Web services
- DevOps workflows

This project reflects:
- Practical problem-solving
- Clean Python standards
- Understanding of external library integration

## Potential Extensions

- CLI argument parsing (argparse)
- Batch processing support
- Logging integration
- REST API wrapper (Flask/FastAPI)
- Docker containerization
- Unit testing (pytest)

## License

MIT License
