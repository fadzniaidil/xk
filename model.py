import sqlite3 as sql
from functools import wraps
from flask import session, flash, redirect, url_for
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fx = os.path.join(BASE_DIR, "edusphere.db")

def signup_user(a, b, c, d):
    with sql.connect(fx) as db:
        qry = 'INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)'
        db.execute(qry, (a, b, c, d))


def login_user(email, password):
    with sql.connect(fx) as db:
        qry = 'SELECT * FROM users WHERE email = ? AND password = ?'
        result = db.execute(qry, (email, password)).fetchone()

        return result

def saving_data(a,b,c,d,e,f,g,h,i):
	with sql.connect(fx) as db:
		qry = 'INSERT INTO subj_grade_form (subj1,subj2,subj3,subj4,subj5,subj6,subj7,subj8,result) VALUES (?, ?, ?, ?,?,?,?,?,?)'
		db.execute(qry, (a, b, c, d,e,f,g,h,i))