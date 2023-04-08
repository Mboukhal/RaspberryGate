#!/var/bin/python

from flask import Flask, request, render_template, flash
from .editFile import setConfig, wifi_disabled
import secrets

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
        if not content['endpoint'] or not content['token']:
            flash('Endpoint and or token is required.')
            return render_template( "index.html" )
        setConfig( content )
        return 'Check if configuration valid.'
    else:
        return render_template( "index.html" )

def startFlask():
    app.run( port=8080 )
    
# if __name__ == '__main__':
#     startFlask()
# if __name__ == '__main__':
#     app.run( debug=True, port=8080 )