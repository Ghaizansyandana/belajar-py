from re import db

class Note(db.Model):
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.String(100), nullabel=False)
    content = db.column(db.String(200), nullable=False)

    def  to_dict(self):
        return{"id": self.id, "title": self.title, "content": self.content}