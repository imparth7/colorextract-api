# Color Extract API

This is a simple RESTful API built with Flask that allows users to upload an image and extract the most prominent colors from it. The API uses the `pixelpalette` library to analyze the image and return a set of colors. This API is open-source and free to use.

## Features

- Upload an image file (PNG, JPG, JPEG).
- Extract a specified number of dominant colors from the image.
- Return the extracted colors in a JSON format.

## Installation

### Prerequisites

- Python 3.x
- pip (Python's package installer)

### Steps to Install

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/color-extract-api.git
   cd color-extract-api
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

- Flask
- PixelPalette
- Werkzeug (for secure filename handling)
- Python Imaging Library (PIL) or Pillow (for image handling)

## Usage

### Running the API Locally

1. Start the Flask server by running the following command:

   ```bash
   python app.py
   ```

   The server will start on `http://0.0.0.0:5000`.

2. Open your browser or use a tool like `Postman` or `curl` to test the API.

### API Endpoints

#### 1. **GET `/`**

- **Description**: This is a simple test endpoint to check if the API is running.
- **Response**:
  ```json
  "Hello, World! This is Color Extract API Free to use, Open-source API"
  ```

#### 2. **POST `/extract-colors`**

- **Description**: Upload an image and extract its prominent colors.
- **Parameters**:

  - **image**: The image file you want to upload. It must be in one of the following formats: PNG, JPG, JPEG.
  - **n_colors** (optional): The number of dominant colors to extract. Default value is `5`.

- **Request Example**:

  - You can use `curl` to send a request:
    ```bash
    curl -X POST -F "image=@your_image.jpg" -F "n_colors=10" http://localhost:5000/extract-colors
    ```

- **Response Example**:

  ```json
  {
    "colors": [
      { "rgb": [255, 0, 0], "hex": "#FF0000" },
      { "rgb": [0, 255, 0], "hex": "#00FF00" },
      { "rgb": [0, 0, 255], "hex": "#0000FF" },
      { "rgb": [255, 255, 0], "hex": "#FFFF00" },
      { "rgb": [0, 255, 255], "hex": "#00FFFF" }
    ]
  }
  ```

- **Error Responses**:
  - **Missing file**: If no image is provided, the API will respond with a 400 error.
    ```json
    {
      "error": "No image file provided"
    }
    ```
  - **Invalid file type**: If the file uploaded is not an image (PNG, JPG, JPEG), the API will return a 400 error.
    ```json
    {
      "error": "Invalid file type"
    }
    ```
  - **Other errors**: If there's an issue during color extraction, a 500 error will be returned with the error message.
    ```json
    {
      "error": "Internal server error"
    }
    ```

## Notes

- The API will temporarily store uploaded images in the `uploads/` directory, then process them and remove them once the colors have been extracted.
- The number of colors (`n_colors`) to be extracted can be customized by passing the value in the request, but it defaults to 5 if not specified.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.