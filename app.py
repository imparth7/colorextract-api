from flask import Flask, request, jsonify
from pixelpalette import extract_colors
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for temporary file uploads
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Function to check allowed file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello_world():
    return "Hello, World!\nThis is Color Extract API Free to use, Open-source API"


@app.route("/extract-colors", methods=["POST"])
def extract_colors_api():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Save the uploaded file temporarily
        file.save(filepath)

        try:
            # Extract colors from the image using PixelPalette
            n_colors = int(
                request.form.get("n_colors", 5)
            )  # Default to 5 colors if not specified
            colors = extract_colors(filepath, n_colors)

            # Clean up the temporary file
            os.remove(filepath)

            return jsonify({"colors": colors}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=False)
