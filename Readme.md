docker build -t bobmortimer_names .

docker run -p 8000:8000 --rm -it -d bobmortimer_names

http://127.0.0.1:8000/v1/name