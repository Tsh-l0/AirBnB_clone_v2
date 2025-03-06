#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """
        Return list of City objects linked to the current State
        """
        from models import storage
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values() if city.state_id == self.id]
        return state_cities
