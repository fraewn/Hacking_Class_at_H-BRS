import json
import os
import sys
import io

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from tempfile import NamedTemporaryFile, TemporaryFile
from flask import Flask, request, render_template, send_file
from lxml import etree

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp"
SOURCE = open(__file__).read()
INDEX = open("templates/index.html").read()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Our secret keys have the form flag{...}
app.secret_key = open("/opt/key.txt")

# man bekommt eine svgfile rein
def convert_svg_png(svgfile):
    # es wird eine temporäre file erstellt
    tmpfile = NamedTemporaryFile(delete=False)
    # dann wird der inhalt der svgfile da rein geschrieben
    tmpfile.write(svgfile.stream.read())
    # dann wird die temporäre file geschlossen
    tmpfile.close()
    # dann wird die lib benutzt und die tempfile wird da rein getan
    drawing = svg2rlg(tmpfile.name)
    os.unlink(tmpfile.name)

    tmp_output = io.BytesIO()
    # dann wird die file in png umgewandelt
    renderPM.drawToFile(drawing, tmp_output, fmt="PNG")
    tmp_output.seek(0)

    response = send_file(
        tmp_output,
        attachment_filename="converted.png",
        mimetype="image/png"
    )
    # und die png file wird mit file name und typ zurück gegeben
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part

        if 'file' not in request.files:
            return "No file uploaded"
        else:
            # die hochgeladene file wird hier abgespeichert
            svgfile = request.files['file']

            # der filename darf kein leerer string sein
            if svgfile.filename == '':
                return "No file provided"

            if svgfile:
                # die file darf iwie nicht zu groß sein
                if os.fstat(svgfile.stream.fileno()).st_size > 400:
                    return "File to big!"
                else:
                    try:
                        # wenn da alles okay ist, wird die convert funktion aufgerufen
                        return convert_svg_png(svgfile)
                    except:
                        return "Error while processing svg file"

    return INDEX


@app.route("/source")
def source():
    return SOURCE, 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run()
