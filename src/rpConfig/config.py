#!/var/bin/python

from flask import Flask, request, render_template, flash
from .editFile import setConfig
import secrets
import os, threading
from .watchFile import watchEnvServer 


from werkzeug.serving import make_server


app = Flask( __name__, template_folder='template', static_folder='static' )
app.secret_key = secrets.token_hex(16)

# app.config['DEBUG'] = False
# os.environ['FLASK_DEBUG'] = '0'

def getData( request ):
    print (request)
    content = {}
    content['endpoint']         = ( request.form['endpoint'] )
    content['token']            = ( request.form['token']    )
    content['token-second']     = ( request.form['token-second']    )
    content['hostname']         = ( request.form['hostname'] )
    return content

@app.route('/', methods=['GET', 'POST'])
def edit_file():

    if request.method == 'POST':
        content = getData( request )
        if not content['endpoint']:
            flash('Endpoint is required.')
            return render_template( "index.html" )
        if not content['token']:
            flash('Token is required.')
            return render_template( "index.html" )
        setConfig( content )
        
        return 'Server shutting down...'
    else:
        return render_template( "index.html" )

gServe = None

def run_flask():
    global gServe
    gServe = make_server('0.0.0.0', 80, app)
    gServe.serve_forever()

def startFlask(env_file):
    
    global gServe
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    if watchEnvServer( env_file ):
        with app.app_context():
            gServe.shutdown()
        flask_thread.join()

