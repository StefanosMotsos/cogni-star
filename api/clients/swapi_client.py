import requests
import logging

logger = logging.getLogger(__name__)

def fetch_swapi_planets():
    url = f"https://swapi.info/api/planets"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info("Fetched %d planets from SWAPI", len(data))
        return data
    except requests.exceptions.RequestException as e:
        logger.exception(f"Error fetching planets")
        return None

def fetch_swapi_people():
    url = f"https://swapi.info/api/people"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info("Fetched %d people from SWAPI", len(data))
        return data
    except requests.exceptions.RequestException as e:
        logger.exception(f"Error fetching people")
        return None
