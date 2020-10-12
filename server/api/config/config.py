class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_NOTIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://bjmashele:securep@wd@localhost:5432/bjmasheledb"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://bjmashele:securep@wd@localhost:5432/bjmasheledb"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://bjmashele:securep@wd@localhost:5432/bjmasheledb"
    SQLALCHEMY_ECHO = False
