# app/models.py

from app import DB




# pylint: disable=no-member

class Bucketlist(DB.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'bucketlists'

    id = DB.Column(DB.Integer, DB.Sequence('bucketlist_id_seq'), primary_key=True)
    name = DB.Column(DB.String(255))
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(
        DB.DateTime, default=DB.func.current_timestamp(),
        onupdate=DB.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        DB.session.add(self)
        DB.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)

