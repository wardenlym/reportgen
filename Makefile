all:
	@python .

image:
	docker build . -t wardenlym/reportgen
