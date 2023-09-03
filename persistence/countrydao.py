from config.database import Session
from models.country import Country


def create_countries(countries):
    session = Session()
    try:
        for country in countries:
            country = Country(**country)
            session.add(country)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
