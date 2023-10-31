from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime, date, timedelta
from NHLProjectFiles import app, db

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")