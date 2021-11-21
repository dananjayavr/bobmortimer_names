import random
import socket
import sys
from fastapi import FastAPI

def get_names_from_file(file):
    """
    Get names from file
    """
    names = []
    with open(file, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names


def choose_random_name(names):
    """
    Choose random name from list
    """
    return random.choice(names)

app = FastAPI()
hostname = socket.gethostname()
version = f"{sys.version_info.major}.{sys.version_info.minor}"

@app.get("/")
async def root():
    return {
        "name": "bobmortimer_names",
        "host": hostname,
        "version": f"From FastAPI running on Uvicorn. Using Python {version}",
        "message": "Welcome to the Bob Mortimer Names API. GET /v1/name to get a random Bob Mortimer name."
    }


@app.get("/v1/name")
async def get_name():
    return {"name":choose_random_name(get_names_from_file('names.txt'))}

# if __name__ == '__main__':
#     names = get_names_from_file('names.txt')
#     for i in range(1):
#         print(choose_random_name(names))