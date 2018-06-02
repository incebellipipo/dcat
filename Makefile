init:
	pip install -r requirements.txt

build:
	./setup.py build

install:
	./setup.py install

clean:
	./setup.py clean --all
