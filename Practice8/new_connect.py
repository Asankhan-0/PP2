import psycopg2
import new_config
def connect_to_db():
    conn = psycopg2.connect(**new_config.login_parameters)
    return conn