from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
import argparse
import base64
import hashlib

DB_FILE_NAME = 'passwords.db'
engine = create_engine(f'sqlite:///{DB_FILE_NAME}')
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)


class Credentials(Base):
    __tablename__ = 'passwords'

    site = Column(String, primary_key=True)
    login = Column(String)
    password = Column(String)

    def __init__(self, site, login, password):
        self.site = site
        self.login = login
        self.password = password


class Passphrase(Base):
    __tablename__ = 'passphrase'

    passphrase = Column(String, primary_key=True)

    def __init__(self, passphrase):
        self.passphrase = passphrase


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def parse_user_input():
    parser = argparse.ArgumentParser(description='Set passphrase -passphrase, input credentials in format --site --login --password. Input --site and -passphase to get pass')
    parser.add_argument("--site", type=str)
    parser.add_argument("--login", type=str)
    parser.add_argument("--password", type=str)
    parser.add_argument("--passphrase", type=str)
    args = parser.parse_args()
    site = args.site
    login = args.login
    password = args.password
    passphrase = args.passphrase
    if passphrase and not site:
        set_passphrase(passphrase)
    if passphrase and site:
        get_credentials(passphrase, site)
    if site and login and password:
        set_credentials(site, login, password)


def set_passphrase(passphrase):
    backuped_passhprase = session.query(Passphrase).all()
    if not backuped_passhprase:
        passphrase = passphrase.encode()
        passphrase = hashlib.md5(passphrase).hexdigest()
        session.add(Passphrase(passphrase))
        session.commit()


def get_credentials(passphrase, site):
    backuped_passhprase = session.query(Passphrase).all()[0]
    backuped_passhprase = backuped_passhprase.passphrase
    passphrase = passphrase.encode()
    if hashlib.md5(passphrase).hexdigest() == backuped_passhprase:
        credentials = session.query(Credentials).filter_by(site=site).first()
        site = credentials.site
        login = credentials.login
        password = credentials.password
        password = get_decoded_pass(password)
        print(f"Site: {site} Login: {login} Password: {password}")
    else:
        print("Incorrect passphrase!")


def set_credentials(site, login, password):
    password = get_encoded_pass(password)
    session.add(Credentials(site, login, password))
    session.commit()


def get_encoded_pass(password):
    password = password.encode()
    password = base64.b64encode(password)
    return password


def get_decoded_pass(password):
    password = base64.b64decode(password).decode()
    return password


if __name__ == "__main__":
    parse_user_input()

