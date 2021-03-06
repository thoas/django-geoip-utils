import django

from django.conf import settings

REQUEST_IP_RESOLVER = getattr(settings, "GEOIP_REQUEST_IP_RESOLVER",
                              "geoip_utils.utils.remote_addr_ip")

CACHE_METHOD = getattr(settings, "GEOIP_CACHE_METHOD", None)
if CACHE_METHOD is None:
    from .compat import GeoIP, has_geoip2

    if django.VERSION < (2, 0) and not has_geoip2:
        CACHE_METHOD = GeoIP.GEOIP_STANDARD
