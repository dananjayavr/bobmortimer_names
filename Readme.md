# Bob Mortimer Names [![Build Status](https://app.travis-ci.com/dananjayavr/bobmortimer_names.svg?branch=main)](https://app.travis-ci.com/dananjayavr/bobmortimer_names)

![Wotsits Wig](https://pbs.twimg.com/media/BXBCXKbIgAAAf3a.jpg)


### Run tests
---
`$ python -m pytest -v tests/test_main.py`

### Build Docker image
---

`docker build -t bobmortimer_names .`

`docker run -p 8000:8000 --rm -it -d bobmortimer_names`


### Push Docker image to Docker Hub
---
`$ docker login -u $USER -p $PASSWORD`

`$ docker build -f Dockerfile -t dananjaya/bobmortimer_names:latest .`

`$ docker push dananjaya/bobmortimer_names:latest`