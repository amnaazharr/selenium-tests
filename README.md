# Selenium Test Setup

This repository contains a basic setup for automated UI testing using Selenium and pytest. It includes tests for adding a product to the cart on the Saucedemo website.

## Prerequisites

- Python 3.11
- Google Chrome
- ChromeDriver
- Selenium
- pytest
- WebDriver Manager

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/selenium-tests.git
    cd selenium-tests
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    conda activate env-name #for linux
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests, use the following command:

```bash
pytest
