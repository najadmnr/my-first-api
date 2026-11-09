from fastapi import FastAPI
import random

app = FastAPI()

# Your API data
quotes = [
    "Believe you can and you're halfway there.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal."
]

@app.get("/")
def get_quote():
    return {"quote": random.choice(quotes)}
