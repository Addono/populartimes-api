# Populartimes API

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Deployment](#deployment)

## About <a name = "about"></a>
A small HTTP server around [m-wrzru/populartimes](https://github.com/m-wrzr/populartimes) to access Google Maps popular times data from the Google Maps SDK. It is designed to run as a serverless function, so hosting a scalable version is trivial!

## Getting Started <a name = "getting_started"></a>
These instructions will get you started using the API. See [deployment](#deployment) for notes on how to deploy your own version.

### Prerequisites
Get a Google Maps SDK key [here](https://developers.google.com/places/web-service/get-api-key).

### Using the API
Throughout these instructions we will use [https://populartimes.now.sh/api/](https://populartimes.now.sh/api/). This version does not have a Google Maps SDK configured, as such we need to set it using the `api_key` query variable. If you decide to host your own version, then you can also pass this as an environment variable, which will remove the need to set it on every request.

The API is simple, there's one endpoint [`/api/`](https://populartimes.now.sh/api/) which takes two query variables:
 * `place_id`: A place ID you have received from another call to the Google Maps API.
 * `api_key` (optional): The Google Maps SDK key want to use. When left empty it is assumed that it's passed as an environment variable in the deployed instance.

### Example

#### Curl
```bash
export PLACE_ID=ChIJSYuuSx9awokRyrrOFTGg0GY # The Place ID you want to query
export API_KEY=... # add your Google Maps API key here
curl 'https://populartimes.now.sh/api/\?place_id\=$PLACE_ID\&api_key\=$API_KEY'
```

#### Browser
Go to [https://populartimes.now.sh/api/?place_id=ChIJSYuuSx9awokRyrrOFTGg0GY&api_key=YOUR_GOOGLE_MAPS_API_KEY](https://populartimes.now.sh/api/?place_id=ChIJSYuuSx9awokRyrrOFTGg0GY&api_key=YOUR_GOOGLE_MAPS_API_KEY) and replace `YOUR_GOOGLE_MAPS_API_KEY` with your Google Maps API Key.

The resulting JSON  will look something like - note this is formatted for readability. See [https://github.com/m-wrzr/populartimes#populartimesget_id](https://github.com/m-wrzr/populartimes#populartimesget_id) for more details on the format of the response.

_Note: Responses might not contain some fields, including `populartimes` and `time_wait` if they are not available for the queried place._
```json
{
  "address": "22 Warren St, New York, NY 10007, USA",
  "coordinates": { "lat": 40.71431500000001, "lng": -74.007766 },
  "id": "ChIJSYuuSx9awokRyrrOFTGg0GY",
  "international_phone_number": "+1 212-577-2725",
  "name": "Gran Morsi",
  "populartimes": [
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 37, 63, 77, 66, 41, 18, 0], "name": "Monday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 52, 78, 93, 90, 69, 43, 0], "name": "Tuesday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 46, 59, 61, 53, 38, 22, 0], "name": "Wednesday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 43, 71, 92, 93, 75, 46, 0], "name": "Thursday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 46, 72, 95, 100, 84, 58, 0], "name": "Friday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 54, 82, 100, 91, 62, 0], "name": "Saturday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 32, 37, 35, 25, 11, 0], "name": "Sunday" }
  ],
  "rating": 4.4,
  "rating_n": 346,
  "time_spent": [90, 180],
  "time_wait": [
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Monday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Tuesday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Wednesday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Thursday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Friday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0], "name": "Saturday" },
    { "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "name": "Sunday" }
  ],
  "types": ["restaurant", "food", "point_of_interest", "establishment"]
}
```

## Deployment <a name = "deployment"></a>

### Vercel
To deploy your own version of the application run:
```bash
now
```

#### Set API Key
If you want to set a default Google Maps API Key, then you need to configure Vercel to use the `GOOGLE_MAPS_API_KEY` environment variable. It is recommended to use secrets, which can be achieved as such:
```bash
# Create now.json
cp now.template.json now.json

# Only needs to be done once per project
now secrets add google-maps-api-key "MY_GOOGLE_MAPS_API_KEY"
```

Now you can deploy as normal and have the Google Maps API key be pre-provisioned. Users can still set the `api_key` on individual requests, which will overwrite the value you configured globally.
