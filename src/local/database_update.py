import asyncio
import websockets
import sqlite3
import json
import os
from get_access import DB_FILE

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

# Add badge to database
def add_badge(badge_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('INSERT OR IGNORE INTO badges (badge_id) VALUES (?)', (badge_id,))
    conn.commit()
    conn.close()

# Remove badge from database
def remove_badge(badge_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM badges WHERE badge_id = ?', (badge_id,))
    conn.commit()
    conn.close()

# Handle received data and update database accordingly
async def process_data(data):
    # if database is not exists, initialize it
    if not os.path.exists(DB_FILE):
        init_db()
    for badge in data.get('data', []):
        badge_id = badge.get('badge-id')
        status = badge.get('status')

        if badge_id:
            if status:
                print(f"Adding badge ID: {badge_id}")
                add_badge(badge_id)
            else:
                print(f"Removing badge ID: {badge_id}")
                remove_badge(badge_id)

# WebSocket client to listen and process incoming messages
async def listen_and_update():

    # token_in = os.getenv("TOKEN_IN")
    # token_out = os.getenv("TOKEN_OUT")
    uri = "ws://localhost:8765"  # WebSocket server URL
    # uri = "ws://" + os.getenv("ENDPOINT")  # WebSocket server URL
    
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to WebSocket")
                
                while True:
                    try:
                        message = await websocket.recv()
                        data = json.loads(message)
                        print(f"Received data: {data}")
                        await process_data(data)
                    except websockets.ConnectionClosed:
                        print("Connection closed, reconnecting...")
                        break  # Break to reconnect to the server
        except Exception as e:
            print(f".")
            await asyncio.sleep(5)  # Wait before retrying

# Initialize database and run WebSocket client
async def main():
    await listen_and_update()

if __name__ == "__main__":
    asyncio.run(main())
