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

## Key Steps in the Project

### 1. Libraries used:
- Selenium: To control the browser and scrape data from dynamic pages (like Lazada).
- BeautifulSoup: To parse and extract data from the HTML.
- Pandas (optional): For handling and saving data in a structured way (like CSV).
- CSV: For writing the product data to a .csv file.
- Datetime: To include the current timestamp in the data.

### 2. Process Flow
- The script loads the Lazada product page using Selenium WebDriver.
- It extracts the product name and price using BeautifulSoup.
- The extracted data is appended to a CSV file with the current timestamp.
- The process is repeated every minute to ensure the data stays up-to-date.

### 3. Handling the Web Scraping
- Selenium is used to load the page and BeautifulSoup to parse the HTML content.
