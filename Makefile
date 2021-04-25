all:
	docker run -v `pwd`:/output wardenlym/reportgen

image:
	docker build . -t wardenlym/reportgen
	docker push wardenlym/reportgen
