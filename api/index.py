from flask import Flask, jsonify, request
import populartimes

import json
import os

app = Flask(__name__)

@app.route('/')
@app.route('/api/')
def catch_all():
  API_KEY = os.environ['GOOGLE_MAPS_API_KEY']

  if not API_KEY:
    return jsonify({"error": "GOOGLE_MAPS_API_KEY env variable not set"})

  place_id = request.args.get('place_id')
  if not place_id:
    return jsonify({"error": "Query argument place_id is required, received '%s'" % place_id})

  try:
    result = populartimes.get_id(api_key=API_KEY, place_id=place_id)
  except Exception as e:
    print(e)
    return jsonify({"message": "Failed accessing the Google Maps SDK", "error": e})

  return jsonify(result)