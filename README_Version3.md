# URL to QR Code Generator

A web-based QR code generator that converts URLs into scannable QR codes. Built with Python, HTML, and CSS.

## Features

- Convert any URL into a QR code
- Clean and simple web interface
- Instant QR code generation
- Download generated QR codes as PNG files
- Works in any modern web browser

## Tech Stack

- **Python** – Backend server and QR code generation
- **HTML & CSS** – Responsive web interface
- **Flask** – Web framework for serving the application

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Salehin-07/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the web server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and visit:**
   ```
   http://localhost:5000
   ```

3. **How to use:**
   - Enter any valid URL in the input field
   - Click "Generate QR Code"
   - Your QR code will be displayed
   - Download the QR code image if desired

## Example

![QR Example](example_qr.png)

## Dependencies

- flask
- qrcode
- pillow

## Project Structure

```
qr-code-generator/
│
├── app.py             # Flask application and QR generation logic
├── requirements.txt   # Python dependencies
├── static/
│   └── style.css     # CSS styling
├── templates/
│   └── index.html    # Main webpage template
└── README.md
```

## Author

- [Salehin-07](https://github.com/Salehin-07)
- Created: 2025-06-10

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Browser Compatibility

Tested and working on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari