include .env

#uvicorn main:app --host $HOST --port $PORT

run:
	uvicorn main:app --host 127.0.0.1 --port 8000