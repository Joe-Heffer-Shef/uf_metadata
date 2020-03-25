import os.path
import datetime
import logging

LOGGER = logging.getLogger(__name__)


class Site(Asset):
    """Physical location"""
    
    def __init__(self, site_id, latitude: float, longitude: float, altitude: float, address, city, country, postcode,
                 first_date: datetime.date, operator: dict, desc_url: str):
        """
        Sensor site (physical location) registered to the Urban Flows Observatory

        :param site_id: unique identifier
        :param latitude: deg
        :param longitude: deg
        :param altitude: height above sea-level in meters
        :param address: [optional]
        :param city: [optional]
        :param country: [optional]
        :param postcode: [optional]
        :param first_date: When the site was commissioned
        :param operator: Who maintains the site
        :param desc_url: Website for further information
        """

        self.id = site_id
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.address = address
        self.city = city
        self.country = country
        self.postcode = postcode
        self.first_date = first_date
        self._operator = operator
        self.desc_url = desc_url

    def __iter__(self):
        yield 'siteid', self.id
        yield 'longitude_[deg]', self.longitude
        yield 'latitude_[deg]', self.latitude
        yield 'height_above_sea_level_[m]', self.altitude
        yield 'address', self.address
        yield 'city', self.city
        yield 'country', self.country
        yield 'Postal_Code', self.postcode
        yield 'firstdate', self.first_date
        yield 'operator', self.operator
        yield 'desc-url', self.desc_url

    @property
    def operator(self) -> str:
        return self.concat_dict(self._operator)
