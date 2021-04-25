all:
	docker run -v `pwd`:/output wardenlym/reportgen

image:
	docker build . -t wardenlym/reportgen
