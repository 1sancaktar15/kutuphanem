
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    genre = db.Column(db.String(length=30), nullable=False, unique=True)
    page = db.Column(db.Integer(), nullable=False,unique=True)
    blurb = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'{self.name}'