#!/var/bin/python

from flask import Flask, request, render_template, flash
from .editFile import setConfig
import secrets
import os

app = Flask( __name__, template_folder='template', static_folder='static' )
app.secret_key = secrets.token_hex(16)

app.config['DEBUG'] = False
os.environ['FLASK_DEBUG'] = '0'


def getData( request ):
    content = {}
    content['endpoint'] = ( request.form['endpoint'] )
    content['token']    = ( request.form['token']    )
    content['relay']    = ( request.form['relay']    )
    content['hostname'] = ( request.form['hostname'] )
    return content


@app.route('/', methods=['GET', 'POST'])
def edit_file():
    if request.method == 'POST':
        content = getData( request )
        if content['relay']:
            try:
                relay = int( content['relay'] )
                if 0 < relay < 28:
                    raise ValueError( "" )
            except ValueError: 
                    flash('relay error.')
                    return render_template( "index.html" )
        if not content['endpoint']:
            flash('Endpoint is required.')
            return render_template( "index.html" )
        if not content['token']:
            flash('Token is required.')
            return render_template( "index.html" )
        setConfig( content )
        return 'Check if configuration valid.'
    else:
        return render_template( "index.html" )


def startFlask():
    app.run( port=80 )


if __name__ == '__main__':
    startFlask()