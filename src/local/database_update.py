import asyncio
import websockets
import sqlite3
import json
import os
from get_access import DB_FILE

import sys

LOG_DIR = '/var/log/gate/'

# Get the parent directory of the current file (which is `src/local`)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (`src`) to the Python path
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))
from logs import log
# file_path = inspect.getfile(inspect.currentframe())
# current_dir = os.path.dirname(os.path.abspath(file_path))
# DB_FILE = os.path.join(current_dir, 'badges.db')


# Initialize SQLite database and create table if not exists
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS badges (
            badge_id TEXT PRIMARY KEY
        )
    ''')
    
    conn.commit()
    conn.close()

# Handle received data and update database accordingly
async def process_data(data):
    # if database is not exists, initialize it
    if not os.path.exists(DB_FILE):
        init_db()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for badge in data.get('data', []):
        badge_id = badge.get('badge-id')
        status = badge.get('status')

        if badge_id is not None and status is not None:
            log(f"Badge ID: {'+' if status else '-'} {badge_id}",  "database_update.log", expiration_days=10)
            if status:
                # print(f"Adding badge ID: {badge_id}")
                # Add or update badge ID in the database
                cursor.execute('INSERT OR IGNORE INTO badges (badge_id) VALUES (?)', (badge_id,))
            else:
                # print(f"Removing badge ID: {badge_id}")
                # Remove badge ID from the database
                cursor.execute('DELETE FROM badges WHERE badge_id = ?', (badge_id,))
        else:
            log(f"Skipping badge ID: {badge_id}",  "database_update.log")
        conn.commit()
    conn.close()


# WebSocket client to listen and process incoming messages
async def listen_and_update():

    uri = "localhost:8765"  # WebSocket server URL
    # uri = os.environ.get("ENDPOINT")

    if not uri:
        log("Missing environment variables: ENDPOINT '%s'" % (uri),  "error.log")
        return
    
    log(f"Connecting to WebSocket server: {uri}",  "database_update.log")
    while True:
        try:
            async with websockets.connect("ws://" + uri) as websocket:
                
                
                while True:

                    try:
                        message = await websocket.recv()
                        data = json.loads(message)
                        # print(f"Received data: {data}")
                        await process_data(data)
                    except websockets.ConnectionClosed:
                        # print("Connection closed, reconnecting...")
                        break  # Break to reconnect to the server
        except Exception as e:
            # print(f".")
            await asyncio.sleep(5)  # Wait before retrying

# Initialize database and run WebSocket client
async def main():
    await listen_and_update()

if __name__ == "__main__":
    asyncio.run(main())
