from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    height = db.Column(db.Integer(), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)

    def to_dict(self):
        return {
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
        }
