import asyncio
import websockets
import json
import random
import string
from datetime import datetime

# Function to generate random badge data with more than 10 items
def generate_random_data():
    num_badges = random.randint(11, 20)  # Random number of badges between 11 and 20
    badges = []
    
    # for _ in range(num_badges):
    badge_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random badge-id
    status = random.choice([True, False])  # Random status (True/False)
    badges.append({
        "badge-id": "RQ8YRYBF",
        "status": True
        })
    
    return {"data": badges}

# Function to send random JSON data every 30 seconds
async def send_json_data(websocket, path):
    while True:
        random_data = generate_random_data()
        json_data = json.dumps(random_data)
        
        await websocket.send(json_data)
        print(f"Sent: {json_data}")
        
        await asyncio.sleep(30)  # Send data every 30 seconds

async def main():
    async with websockets.serve(send_json_data, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run the server forever

if __name__ == "__main__":
    asyncio.run(main())
