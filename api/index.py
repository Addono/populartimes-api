from flask import Flask, jsonify, request
import populartimes

import json
import os

app = Flask(__name__)

@app.route('/')
@app.route('/api/')
def catch_all():
  api_key = request.args.get('api_key') or os.environ['GOOGLE_MAPS_API_KEY']

  if not api_key:
    return jsonify({"error": "Google Maps API key not passed, please set it using api_key query argument."})

  place_id = request.args.get('place_id')
  if not place_id:
    return jsonify({"error": "Query argument place_id is required, received '%s'" % place_id})

  try:
    result = populartimes.get_id(api_key=api_key, place_id=place_id)
  except Exception as e:
    print(e)
    return jsonify({"message": "Failed accessing the Google Maps SDK", "error": e})

  return jsonify(result)