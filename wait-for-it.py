"""wait-for-it.py - Entrypoint PostgreSQL.

Site: https://github.com/DiegoBulhoes/entrypoint-postgresql
Autor: DiegoBulhoes <https://github.com/DiegoBulhoes/>
"""
import time
import os

import subprocess as ps
import psycopg2 as pg

from dotenv import load_dotenv
from time import sleep

from sys import argv as arg


def load_environment(path_env_file):
    """Load variables into the environment."""
    envPath = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), path_env_file)
    load_dotenv(envPath)


def connection_database():
    """Establish a connection to PostgreSQL.

    Returns:
        connection object -- object that allows connection to the bank
    """
    return pg.connect(dbname=os.environ['DB_NAME'],
                      user=os.environ['DB_USER'],
                      host=os.environ['DB_IP'],
                      password=os.environ['DB_PASSWORD'],
                      connect_timeout=os.environ['CONNECT_TIMEOUT'])


def timeout(tic, toc):
    """
    Check if a timeout occurred according to the past parameters.

    Arguments:
        tic {float} -- start time a timer
        toc {float} -- end time a stopwatch.

    Returns:
        boolean -- Returns true if the timeout was not given,
                    otherwise false will be returned.
    """
    return (toc-tic) > int(os.environ['CONNECT_TIMEOUT'])


def is_server_up(path_env_file, toc):
    """Check if the service is running.

    Arguments:
        toc {float} -- end time a stopwatch.
    """
    while True:
        try:
            tic = time.time()
            load_environment(path_env_file)
            conn = connection_database()
            cmd = os.environ['CMD_APP']
            ps.run(cmd.split(), shell=False, check=True)
            conn.close()
            print("Postgres is up - executing command.")
        except pg.OperationalError:
            print(' Error establishing connection')
        except BaseException:
            print('Unexpected error')
        finally:
            if timeout(tic, toc):
                Exception("Timeout")
                break
            sleep(10)


if __name__ == "__main__":
    toc = time.time()
    is_server_up(path_env_file=arg[1], toc=time.time())
