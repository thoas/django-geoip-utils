from django.utils.functional import LazyObject

from .utils import get_ip_of_request
from .settings import CACHE_METHOD
from .compat import GeoIP


class GeoIPHandler(LazyObject):

    def _setup(self):
        if CACHE_METHOD:
            self._wrapped = GeoIP(cache=CACHE_METHOD)
        else:
            self._wrapped = GeoIP()

geoip = GeoIPHandler()


def get_country(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country(ip)


def get_city(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.city(ip)


def get_lat_lon(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.lat_lon(ip)


def get_country_code(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_code(ip)


def get_country_name(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_name(ip)
