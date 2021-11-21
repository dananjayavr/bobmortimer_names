# Bob Mortimer Names [![Build Status](https://app.travis-ci.com/dananjayavr/bobmortimer_names.svg?branch=main)](https://app.travis-ci.com/dananjayavr/bobmortimer_names)

![Wotsits Wig](https://pbs.twimg.com/media/BXBCXKbIgAAAf3a.jpg)


### Run tests
---
`$ python -m pytest -v tests/test_main.py`

### Build & run Docker image
---

`$ docker build -t bobmortimer_names .`

`$ docker run -p 8000:8000 --rm -it -d bobmortimer_names`


### Build & push Docker image to Docker Hub
---
`$ docker login -u $USER -p $PASSWORD`

`$ docker build -f Dockerfile -t dananjaya/bobmortimer_names:latest .`

`$ docker push dananjaya/bobmortimer_names:latest`


### Push Docker image to Heroku
---
`$ heroku login`

`$ heroku create`

`$ heroku plugins:install @heroku-cli/plugin-container-registry`

`$ heroku container:login`

`$ heroku container:push web`

`$ heroku container:release web`


### Original Inspiration 
---
[How to build a modern CI/CD pipeline - Rob van der Leek](https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b) 