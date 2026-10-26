import http.server
import socketserver
import urllib.parse
import os
from image_captioning import load_model, load_image, generate_caption, save_caption

PORT = 8000

print("Loading model... This might take a few moments.")
processor, model = load_model()
print("Model loaded.")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Captioning Server</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .container {{ max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; }}
        input[type="file"] {{ width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }}
        input[type="submit"] {{ padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }}
        .result {{ margin-top: 20px; padding: 15px; background-color: #f8f9fa; border-left: 5px solid #007bff; }}
        img {{ max-width: 100%; height: auto; border-radius: 5px; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Image Captioning System (Local Server)</h2>
        <form method="POST" action="/" enctype="multipart/form-data">
            <label for="image_file">Upload an image from your computer:</label>
            <input type="file" id="image_file" name="image_file" accept="image/*" required>
            <input type="submit" value="Upload and Generate Caption">
        </form>
        {result}
    </div>
</body>
</html>
"""

class CaptioningHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = HTML_TEMPLATE.format(result="")
            self.wfile.write(html.encode("utf-8"))
        else:
            # Serve static files (like images in the directory)
            super().do_GET()

    def do_POST(self):
        if self.path == '/':
            content_type = self.headers.get('Content-Type')
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            result_html = ""
            image_path = None

            if content_type and 'multipart/form-data' in content_type:
                from email import message_from_bytes
                
                # Add headers so email.message_from_bytes can parse it
                msg_bytes = f"Content-Type: {content_type}\r\n\r\n".encode('utf-8') + post_data
                msg = message_from_bytes(msg_bytes)
                
                uploaded_file = None
                filename = None
                for part in msg.walk():
                    if part.get_filename():
                        filename = part.get_filename()
                        uploaded_file = part.get_payload(decode=True)
                        break
                
                if uploaded_file and filename:
                    # Save the uploaded file temporarily
                    os.makedirs("uploads", exist_ok=True)
                    # secure filename
                    filename = os.path.basename(filename)
                    image_path = os.path.join("uploads", filename)
                    with open(image_path, "wb") as f:
                        f.write(uploaded_file)
            else:
                result_html = '<div class="result" style="border-left-color: red;"><p>Invalid form submission. Please upload a file.</p></div>'

            if image_path:
                image = load_image(image_path)
                if image:
                    caption = generate_caption(processor, model, image)
                    if caption:
                        # Ensure forward slashes for URLs
                        img_url = image_path.replace('\\', '/')
                        result_html = f'''
                        <div class="result">
                            <h3>Result:</h3>
                            <p><strong>Caption:</strong> {caption.capitalize()}.</p>
                            <img src="/{img_url}" alt="Image">
                        </div>
                        '''
                        save_caption(image_path, caption)
                    else:
                        result_html = '<div class="result" style="border-left-color: red;"><p>Failed to generate caption.</p></div>'
                else:
                    result_html = f'<div class="result" style="border-left-color: red;"><p>Could not load image.</p></div>'
                    
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = HTML_TEMPLATE.format(result=result_html)
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), CaptioningHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
