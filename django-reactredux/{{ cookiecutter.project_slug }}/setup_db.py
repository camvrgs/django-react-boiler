#!/usr/bin/env python
"""
Using psycopg2 Create Postgres DB
"""

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
  dbname='{{ cookiecutter.server_postgres_db_name }}'
  # to establish connection, use default 'postgres' db
  connection = psycopg2.connect(
    dbname='postgres',
    user='{{ cookiecutter.server_postgres_username }}',
    password='{{ cookiecutter.server_postgres_pass }}',
    host='{{ cookiecutter.server_postgres_host }}',
    port='{{ cookiecutter.server_postgres_port }}'
  )

  # Set Autocommit
  connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

  with connection.cursor() as cur:

    # Best to use psycopg2.sql of string concatenation
    # to prevent sql injection attacks
    cur.execute(sql.SQL('CREATE DATABASE {}').format(
      sql.Identifier(dbname))
    )

  connection.close()

except psycopg2.errors.DuplicateDatabase:
  pass

except psycopg2.OperationalError as e:
  print('Error occurred on database creation:')
  print(e)
