# Industry News App

This project is a minimalistic web application that displays news by industry using the [GNews](https://github.com/ranahaani/GNews) library.

## Features
- Choose from a list of industries (Finance, HVAC, Automotive, Technology, Sports).
- Fetches news articles from GNews API and stores them as JSON files under `news/`.
- Simple and modern interface built with HTML, CSS and JavaScript.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000` in your browser and select an industry to see the latest news.

JSON files are saved to the `news/` directory when news is fetched.
