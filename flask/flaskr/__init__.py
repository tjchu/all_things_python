import os

from flask import Flask, render_template, url_for


def create_app(test_config=None):
    app.config['SECRET_KEY'] = ''


    posts = [
        {
            'author': 'Terry Chu',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'April 20, 2018',

        },
        {
            'author': 'Sarah Chu',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'April 21, 2018',

        }
    ]

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html', posts=posts)

    @app.route('/about')
    def about():
        return render_template('about.html', title='About')

    return app
