# 📊 PriceCharting CAD Price Scraper

This Python script scrapes the ungraded USD price of any product from [PriceCharting](https://www.pricecharting.com), converts it to CAD using live exchange rates, and prints clean copy-pasteable prices for use in spreadsheets like Google Sheets.

---

## 🔧 Requirements

- Python 3.8+
- Google Chrome (installed)
- ChromeDriver (automatically managed via `webdriver-manager`)

---

## 🛠 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Jugtojssidhu/pricecharting-scraper.git
    cd pricecharting-scraper
    ```

2. **Install the required Python packages:**

    ```bash
    pip install selenium webdriver-manager requests
    ```

---

## 🚀 Usage

1. Open `Scraper.py` in your text editor.
2. Paste your PriceCharting product URLs inside the `urls = [ ... ]` list.
3. Run the script from the terminal:

    ```bash
    python Scraper.py
    ```

✅ It will open a headless Chrome browser, scrape each product’s ungraded USD price, convert it to CAD, and print the results line by line.

---

## 📋 Example Output

228.58 
114.30 
31.43 
190.45

Copy-paste those values directly into your Google Sheets price tracker.

---

## 📁 File Description

| File        | Description                                        |
|-------------|----------------------------------------------------|
| `Scraper.py` | The full script to scrape and convert PriceCharting prices |

---

## 🧠 Tip

To reduce wait time, the script reuses the same browser session and only loads the exchange rate once — giving you maximum speed with minimal overhead.

---

## 🔒 License

This project is open-source and free to use for personal or educational projects. Please credit if shared or modified.

