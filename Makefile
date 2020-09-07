all:


clean:
	rm build dist -r
	rm *.egg-info -r

install:
	python setup.py install