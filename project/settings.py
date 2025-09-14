import flask
import os


project = flask.Flask(
    import_name = 'project',
    static_url_path= '/static',
    static_folder = 'static',
    template_folder = 'templates',
    instance_path = os.path.abspath(os.path.join(__file__,'..','instance'))
)