from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    animal = db.relationship('Animal', backref='zookeepers', lazy=True)

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    environment  = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    enclosed_animals = db.relationship('Animal', backref='enclosures', lazy=True)

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    species = db.Column(db.String(20), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure = db.relationship('Enclosure', backref='animals', lazy=True)
    zookeeper = db.relationship('Zookeeper', backref='animals', lazy=True)  
