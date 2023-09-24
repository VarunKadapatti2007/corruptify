from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        filename = request.form['filename']
        extension = request.form['extension']
        size_kb = int(request.form['size_kb'])

        # Create a corrupted file with the given attributes
        corrupted_file_path = create_corrupted_file(filename, extension, size_kb)

        # Send the corrupted file as a response
        return send_file(corrupted_file_path, as_attachment=True, download_name=f'{filename}.{extension}')

    return render_template('index.html')

def create_corrupted_file(filename, extension, size_kb):
    # Calculate the size in bytes
    size_bytes = size_kb * 1024

    # Create a corrupted file with the given size (filled with null bytes)
    file_path = f'static/{filename}.{extension}'
    with open(file_path, 'wb') as file:
        file.write(b'\0' * size_bytes)

    return file_path

if __name__ == '__main__':
    app.run(debug=True)
