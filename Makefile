test:
	coverage run --branch --source=geoip_utils manage.py test geoip_utils
	coverage report --omit=geoip_utils/test*

release:
	python setup.py sdist register upload -s
