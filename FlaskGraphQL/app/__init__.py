from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


if __name__ == 'main':
    app = Flask(__name__)

    @app.route("/")
    def test():
        return "Test ok!"
