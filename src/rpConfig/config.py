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
        # if os.path.exists( ".env" ):
        #     func = request.environ.get('werkzeug.server.shutdown')
        #     if func is None:
        #         raise RuntimeError('Not running with the Werkzeug server')
        #     func()
        return 'Server shutting down...'
    else:
        return render_template( "index.html" )

gServe = None

def run_flask():
    global gServe
    gServe = make_server('0.0.0.0', 80, app)
    gServe.serve_forever()

def startFlask():
    
    global gServe
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # app.run( host='0.0.0.0', port=80 )
    print ( "OK!" )
    if watchEnvServer( '.env' ):
        with app.app_context():
            gServe.shutdown()
        flask_thread.join()
    
    # try:
    #     app.run( host='0.0.0.0', port=80 )
    # except exit_flask:
    #     print( exit_flask )


# if __name__ == '__main__':
#     startFlask()