from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    videos = [
        {"url": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFGNW.mp4", "title": "GLOBONEWS"},
        {"url": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFGNT.mp4", "title": "GNT"},
        {"url": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFSPO.mp4", "title": "SPORTV"},
        {"url": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFMSW.mp4", "title": "MULTISHOW"},
        {"url": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFVIVA.mp4", "title": "VIVA"}
    ]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
