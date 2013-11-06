from django.test import TestCase


class GeoIpDataTestCase(TestCase):
    def test_country(self):
        from ..templatetags import geoip_tags

        request = type('lamdbaobject', (object,), {
            'META': {'REMOTE_ADDR': '1.1.1.1'},
        })()

        geoip_tags.country_of_request(request)
