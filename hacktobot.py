"""
	Server to listen to pull requests using GitHub webhooks.
	
	Outer shell to co-ordinate between all other actions
"""

from flask import Flask, request, abort
from json import dump
import hmac
import hashlib
import os

app = Flask(__name__)

GITHUB_SECRET = os.environ['GITHUB_SECRET']

@app.route("/")
def home():
	return "Webhook is up and running!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':

		# Extract signature header
		signature = request.headers.get("X-Hub-Signature")
		if not signature or not signature.startswith("sha1="):
			abort(400, "X-Hub-Signature required")

		# Create local hash of payload
		digest = hmac.new(GITHUB_SECRET.encode(), request.data, hashlib.sha1).hexdigest()

		# Verify signature
		if not hmac.compare_digest(signature, "sha1=" + digest):
			abort(400, "Invalid signature")

		if(request.json['action'] == 'open'):
			pass

			# request.json['number'] gives the PR number

			# TODO: Check if the PR is valid
			# TODO: Check for the files
			# TODO: Execute and send the output on discord
		

		return 'success', 200
	else:
		abort(400)