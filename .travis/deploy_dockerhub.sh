#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "main" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t $DOCKER_USER/$TRAVIS_REPO_SLUG:$TAG .
docker push $DOCKER_USER/$TRAVIS_REPO_SLUG:$TAG