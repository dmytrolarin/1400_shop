import flask


def render_catalog():
    return flask.render_template('catalog.html')