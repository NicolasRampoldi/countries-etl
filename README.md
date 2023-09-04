# Countries ETL


This Python project allows you to collect country data from the [rest countries API](https://restcountries.com/v3.1/all), store it in a database, generate an Excel file with the data and send it via email.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.x
- PostgreSQL
- Python dependencies (see requirements.txt)

## Installation

1. Clone the repository and enter the project folder:

   ```bash
   git clone git@github.com:NicolasRampoldi/countries-etl.git
   cd countries-etl
   ```
2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies:

   ```bash
    pip install -r requirements.txt
    ```
   
4. Create a PostgreSQL database and run the script provided in /persistence/resources/schema.sql then set the following environment variables in /config/.env:

    ```bash
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    DB_NAME=
    SMTP_SERVER=
    SMTP_PORT=
    SMTP_USERNAME=
    SMTP_PASSWORD=
    ```
   
## Usage

1. To run the project once, execute the following command in the root folder:

    ```bash
    python3 main.py
    ```
   
2. To run the project periodically once per day, execute the following command in the root folder:

    ```bash
    python3 main.py --daily
    ```

## Possible improvements

- Add unit tests
- Add logging
- Add more error handling