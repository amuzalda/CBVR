from flask import Flask, request, send_from_directory
from search import searchVideo
# set the "static" directory as the static folder.
# this will ensure that all the static files are under one folder
app = Flask(__name__, static_url_path='/static')

# serving some static html files
@app.route('/hello')
def send_html():
    return jsonify(message = "Hello")


@app.route('/upload', methods=['POST'])
def upload_file():
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    file = request.files['file']
    print (file.filename)
    file.save("uploadedFiles/"+file.filename)
    # TODO: call cbvr function this is written by anmol new content
    response_filenames = searchVideo(file.filename)
    #
    print (response_filenames)

    # return response_filenames
    return "file uploaded"
    # [/home/ankita/btp7/CBVR/data/BIKE/cycle1.avi, /home/ankita/btp7/CBVR/data/BIKE/cycle1.avi]

if __name__ == "__main__":
    app.run()
