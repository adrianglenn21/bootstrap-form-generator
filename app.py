from flask import render_template, request, url_for, redirect, flash, send_file
from utils.shell import *
from utils.general import *
from settings import *
from routes import register_blueprints
register_blueprints(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'app': app,
        'generate_models': generate_models,
    }

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
