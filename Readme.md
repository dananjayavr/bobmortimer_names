docker build -t bobmortimer_names .

docker run -p 8000:8000 --rm -it -d bobmortimer_names

http://127.0.0.1:8000/v1/name

docker login -u $USER -p $PASSWORD

build -f Dockerfile -t dananjaya/bobmortimer_names:latest .

docker push dananjaya/bobmortimer_names:latest