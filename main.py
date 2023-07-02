import click
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geoip import geolite2
import os
import logging
from datetime import datetime
from iptables_manager import IPTablesManager
from vulnerable_urls import vulnerable_urls
from ipaddress import ip_address, IPv4Network

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
db = SQLAlchemy(app)
iptables_manager = IPTablesManager()

logging.basicConfig(filename='app.log', level=logging.INFO)

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


def create_tables() -> None:
    """Create all tables in the database."""
    db.create_all()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path: str) -> tuple:
    print("hey")
    """
    Catch all route that logs all incoming requests and blocks any IP that tries to access a suspicious URL.

    Parameters
    ----------
    path : str
        The path of the incoming request.

    Returns
    -------
    tuple
        A tuple containing a JSON response and a status code.
    """
    ip_address_str = request.remote_addr
    url = request.url
    headers = dict(request.headers)
    cookies = request.cookies

    # Check if the IP address is a real one and not an internal one
    try:
        ip_address_obj = ip_address(ip_address_str)
        if ip_address_obj.is_private or ip_address_obj.is_loopback or ip_address_obj.is_link_local:
            return jsonify({"message": "Request logged"}), 200
    except ValueError:
        return jsonify({"message": "Invalid IP address"}), 400

    match = geolite2.lookup(ip_address_str)
    country = match.country if match else "Unknown"

    for pattern, is_regex in vulnerable_urls:
        if (is_regex and re.search(pattern, url)) or (not is_regex and pattern in url):
            blocked_ip = BlockedIP(ip_address=ip_address_str, request_id=request_log.id)
            db.session.add(blocked_ip)
            db.session.commit()
            logging.info(f"Blocked IP: {ip_address_str}")
            iptables_manager.block_ip(ip_address_str)
            return jsonify({"message": "IP blocked"}), 403

    request_log = RequestLog(
        ip_address=ip_address_str,
        url=url,
        headers=str(headers),
        cookies=str(cookies),
        country=country
    )
    db.session.add(request_log)
    db.session.commit()
    logging.info(f"Logged request from IP: {ip_address_str}")

    return jsonify({"message": "Request logged"}), 200

@app.cli.command("unban")
@click.argument("ip")
def unban(ip: str) -> None:
    """
    Unban an IP address.

    Parameters
    ----------
    ip : str
        The IP address to unban.
    """
    blocked_ip = BlockedIP.query.filter_by(ip_address=ip).first()
    if blocked_ip:
        db.session.delete(blocked_ip)
        db.session.commit()
        iptables_manager.unblock_ip(ip)
        print(f"Unbanned IP: {ip}")
    else:
        print(f"No such IP: {ip} in blocked list")

if __name__ == '__main__':
    if not os.path.exists('app.db'):
        db.create_all()
    app.run(debug=True)