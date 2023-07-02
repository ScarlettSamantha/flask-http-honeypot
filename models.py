from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class BlockedIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    request_id = db.Column(db.Integer, db.ForeignKey('request_log.id'), nullable=False)

class RequestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    url = db.Column(db.String(500), nullable=False)
    headers = db.Column(db.String(500), nullable=False)
    cookies = db.Column(db.String(500), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    blocked_ips = db.relationship('BlockedIP', backref='request', lazy=True)