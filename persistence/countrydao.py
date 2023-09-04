from config.database import Session
from models.country import Country


def create_countries(countries):
    session = Session()
    try:
        for country in countries:
            country = Country(**country)
            # Used merge to avoid errors when the country already exists
            session.merge(country)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_countries():
    session = Session()
    try:
        countries = session.query(Country).all()
        return countries
    except Exception as e:
        raise e
    finally:
        session.close()
