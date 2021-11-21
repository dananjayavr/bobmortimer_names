import random
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

@app.get("/")
async def root():
    return {"message": "GET /v1/name to get a random Bob Mortimer name."}

@app.get("/v1/name")
async def get_name():
    return {"name":choose_random_name(get_names_from_file('names.txt'))}


# if __name__ == '__main__':
#     names = get_names_from_file('names.txt')
#     for i in range(1):
#         print(choose_random_name(names))