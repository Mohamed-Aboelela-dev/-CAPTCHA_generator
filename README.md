# CAPTCHA Verification Script

This Python script generates a random CAPTCHA image using uppercase letters and digits, displays it to the user, and prompts for manual verification through terminal input.

## Features

- Generates 8-character CAPTCHA codes using uppercase letters and numbers.
- Uses `captcha` and `Pillow (PIL)` to generate and display CAPTCHA images.
- Supports multiple fonts and sizes for a more realistic CAPTCHA appearance.
- Saves the generated CAPTCHA as `CAPTCHA.png` and opens it automatically.

## Requirements

- Python 3.x
- `captcha` library
- `Pillow` (PIL) library

## Installation

1. **Clone this repository:**

   ```bash
   git clone <git@github.com:Mohamed-Aboelela-dev/CAPTCHA_generator.git>
   cd -CAPTCHA_generator
   ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using:
```bash
python main.py
