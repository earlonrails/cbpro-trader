.PHONY: clean test install

install:
	docker build -t cbpro .

test:
	docker run -v ${PWD}:/app cbpro python3 -m unittest

clean:
	docker image rm cbpro
