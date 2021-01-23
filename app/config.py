from os import environ


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIMULATE_NETWORK_LATENCY = environ.get("SIMULATE_NETWORK_LATENCY", "").lower() == "true"