import os
from dotenv import load_dotenv
from binance.client import Client


load_dotenv()


class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise Exception("API keys are missing. Check your .env file.")

        self.client = Client(
            self.api_key,
            self.api_secret,
            testnet=True
        )

    def get_client(self):
        return self.client