#!/usr/bin/python

import os
import sqlite3
import urllib.request

# Remote database information
REMOTE_DB_URL = "http://example.com/mydatabase.db"

# Local database information
LOCAL_DB_FILENAME = "mydatabase.db"

def main():
    remote_conn = sqlite3.connect(urllib.request.urlopen(REMOTE_DB_URL).read())
    local_conn = sqlite3.connect(LOCAL_DB_FILENAME)

    if not are_databases_equal(remote_conn, local_conn):
        create_local_database(remote_conn)

    remote_conn.close()
    local_conn.close()

def are_databases_equal(remote_conn, local_conn):
    remote_tables = get_table_names(remote_conn)
    local_tables = get_table_names(local_conn)

    return set(remote_tables) == set(local_tables)

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [table[0] for table in cursor.fetchall()]

def create_local_database(remote_conn):
    temp_filename = LOCAL_DB_FILENAME + ".temp"

    try:
        urllib.request.urlretrieve(REMOTE_DB_URL, temp_filename)

        if os.path.exists(LOCAL_DB_FILENAME):
            os.remove(LOCAL_DB_FILENAME)

        os.rename(temp_filename, LOCAL_DB_FILENAME)

    except Exception as e:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

        raise Exception("Unable to create local database: " + str(e))

if __name__ == "__main__":
    # main()
    print( "ok cron" )
