import os
import shutil
from flask import Flask, render_template
from flask_frozen import Freezer

def generate_app():
    app = Flask(__name__)
    filenames = os.listdir('templates/')
    ignore = ['default.html']
    filenames = [filename for filename in filenames if filename not in ignore]
    filenames = [filename for filename in filenames if 'swp' not in filename]

    for filename in filenames:
        if filename == 'index.html':
            path = '/'
        else:
            path = '/' + filename
        @app.route(path)
        def route():
            return render_template(filename)
    return app
        
if __name__ == '__main__':
    APP = generate_app()
    APP.config['FREEZER_REMOVE_EXTRA_FILES'] = True
    APP.config['FREEZER_DESTINATION_IGNORE'] = ['.git', 'CNAME', 'favicon.ico']
    freezer = Freezer(APP)
    Freezer(APP).freeze()
