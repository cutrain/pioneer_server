from . import app, db
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Users(db.Model):
    __tablename__ = 'Users'
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(256))
    iconlink = db.Column(db.String(256))
    posts = db.relationship('Posts', backref='user', lazy=True)
    replies = db.relationship('Replies', backref='user', lazy=True)

    def __repr__(self):
        return "<Users %r>" % self.username

    def generate_token(self, expiration=600):
        token = {'id':self.userId,
                 'time':time.time(),
                }
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps(token)

    @staticmethod
    def verify(token):
        try:
            s = Serializer(app.config['SECRET_KEY'])
            data = s.loads(token)
            now_t = time.time()
            if now_t - data['time'] > data['expiration']:
                return None
            user = Users.query.get(data['id'])
            return user
        except Exception:
            return None




class Posts(db.Model):
    __tablename__ = 'Posts'
    postId = db.Column(db.Integer, primary_key=True)
    postTitle = db.Column(db.String(50), nullable=False)
    postTime = db.Column(db.DateTime, nullable=False)
    forumName = db.Column(db.String(50), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('Users.userId'))

    def __repr__(self):
        return '<Posts %r>' % self.postTitle


class Replies(db.Model):
    __tablename__ = 'Replies'
    replyId = db.Column(db.Integer, primary_key=True)
    replyToId = db.Column(db.Integer, nullable=False)
    replyTime = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    floor = db.Column(db.Integer, nullable=False, unique=True)
    postId = db.Column(db.Integer, db.ForeignKey('Posts.postId'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('Users.userId'), nullable=False)

    def __repr__(self):
        return '<Replies %r>' % self.content


Likes = db.Table(
    'Likes',
    db.Column('userId', db.Integer, db.ForeignKey('Users.userId'), primary_key=True),
    db.Column('replyId', db.Integer, db.ForeignKey('Replies.replyId'), primary_key=True),
)


Favorates = db.Table(
    'Favorates',
    db.Column('userId', db.Integer, db.ForeignKey('Users.userId'), primary_key=True),
    db.Column('PostId', db.Integer, db.ForeignKey('Posts.postId'), primary_key=True),
)

