include .env

reqs = requirements.txt
compile_settings = --output ${reqs} --without-hashes

compile-core-requirements:
	poetry export -f ${reqs} ${compile_settings}

run: compile-core-requirements
	pip install -r ${reqs}
	uvicorn main:app --host ${HOST} --port ${PORT}