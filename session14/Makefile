
prepare: 
	rm -rf .venv
	uv python install 3.12
	uv python pin 3.12
	uv sync


install:
	uv add crewai 

run:
	uv crewai run