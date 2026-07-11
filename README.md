# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot for Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders through a command-line interface.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Logging of API requests and responses
- Exception handling
- Environment variables using .env

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env

## Installation

1. Clone the repository.

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment.

Windows PowerShell:

.\venv\Scripts\Activate.ps1

4. Install dependencies:

pip install -r requirements.txt

5. Create a `.env` file:

API_KEY=your_api_key

API_SECRET=your_api_secret

## Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

## Assumptions

- Uses Binance Futures Testnet API.
- API credentials are stored in a `.env` file.
- Python version: 3.13

## Logging

Logs are stored in:

logs/trading.log