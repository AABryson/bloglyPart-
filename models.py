from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db=SQLAlchemy()


def connect_db(app):
    db.app=app
    db.init_app(app)


"""Models for Blogly."""
#class will be mapped to a table
class User(db.Model):
    __tablename__ = "users"
    #columns of table are class attributes; specify datatypes and constraints
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20),
                           nullable=False)
    last_name = db.Column(db.String(20),
                          nullable=False)
    #default image?
    picture = db.Column(db.Text,
                          nullable=False)
    

    #method??????????????????????

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.picture}>"