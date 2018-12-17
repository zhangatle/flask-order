# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue())
    mobile = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False)
    email = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String(64, 'utf8mb4_general_ci'), nullable=False)
    login_name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, unique=True)
    login_pwd = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False)
    login_salt = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
