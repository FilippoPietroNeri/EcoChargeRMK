from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime, timedelta
import requests

import utils.config as cfg

app = Flask(__name__)
app.secret_key = cfg.SECRET_KEY