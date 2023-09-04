import argparse
import time

import schedule

from persistence.countrydao import create_countries, get_countries
from scripts.country_data import get_country_data
from scripts.email_sender import send_email
from scripts.excel_generator import generate_excel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", help="Daily email report", action="store_true")
    args = parser.parse_args()

    countries = get_country_data()

    create_countries(countries)

    countries_from_db = get_countries()

    generate_excel(countries_from_db)

    receiver_email = "test@gmail.com"
    subject = "Datos de Países"
    message = "Adjunto archivo con los datos de países y gráfico con población por continente."
    attachment_path = "assets/countries_data.xlsx"

    if args.daily:
        schedule.every().day.at("10:00").do(send_email)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        send_email(receiver_email, subject, message, attachment_path)

if __name__ == "__main__":
    main()
