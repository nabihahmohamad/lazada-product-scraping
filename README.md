# Lazada Product Scraper

This project is a Python script that scrapes product details (Product Name, Price, and Timestamp) from a Lazada product page and saves the data into a CSV file. The script runs continuously, retrieving data every 1 minute and appending it to the CSV file.

## Features

- Scrapes product information from a Lazada product page.
- Extracts product name, price, and timestamp.
- Saves the data into a CSV file.
- Runs every 1 minute to capture fresh data.
- Simple and easy-to-use with Selenium and Python.

## Requirements

Before running the script, you will need to install the required libraries:

- **Python 3.x**
- **Selenium** for web scraping
- **webdriver-manager** for handling ChromeDriver
- **datetime** for timestamps
- **CSV** for data storage

You can install the required Python libraries using pip:

```bash
pip install selenium webdriver-manager
