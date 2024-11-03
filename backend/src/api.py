"""
This file defines the FastAPI app for the API and all of its routes.
To run this API, use the FastAPI CLI
$ fastapi dev src/api.py
"""
import beaches
import random
import pysurfline

from beaches import get_zip
from weatherapi import pull_data
from fastapi import FastAPI

APIKEY = "a0a0e8d9da8256bbec2e9eb46469f08b"
# The app which manages all of the API routes
app = FastAPI()


# The decorator declares the function as a FastAPI route on the given path.
# This route in particular is a GET route at "/hello" which returns the example
# dictionary as a JSON response with the status code 200 by default.
@app.get("/hello")
def hello() -> dict[str, str]:
    """Get hello message."""
    return {"message": "Hello from FastAPI"}


# The routes that you specify can also be dynamic, which means that any path
# that follows the format `/items/[some integer]` is valid. When providing
# such path parameters, you'll need to follow this specific syntax and state
# the type of this argument.
#
# This path also includes an optional query parameter called "q". By accessing
# the URL "/items/123456?q=testparam", the JSON response:
#
# { "item_id": 123456, "q": "testparam" }
#
# will be returned. Note that if `item_id` isn't an integer, FastAPI will
# return a response containing an error statement instead of our result.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}


@app.get("/get-random")
def get_random_item() -> dict[str, int]:
    """Get an item with a random ID."""
    return {"item_id": random.randint(0, 1000)}


@app.get("/tide-data")
def get_tides(beach_name: str):
    spotId =  beaches.get_beach_id(beach_name)
    print(spotId)

    if not(spotId):
        return "Not a beach nearby"
    spotforecasts = pysurfline.get_spot_forecasts(spotId)
    return spotforecasts.tides

@app.get("/basic-weather-stats")
def get_weather(beach_name):
    zipcode = get_zip(beach_name)
    return pull_data(zipcode, APIKEY)