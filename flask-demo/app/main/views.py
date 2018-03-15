# -*- encoding: utf-8 -*-

from flask import render_template, send_from_directory, current_app, request
import config
from app.models import User
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/queryone', methods=['POST', 'GET'])
def index():
    username = request.args.get('username')
    User = User.query.filter_by(aid=username).first()
    current_app.logger.info(User)

@main.route('/queryall', methods=['POST', 'GET'])
def index():
    users = User.query.all()
    current_app.logger.info(users)