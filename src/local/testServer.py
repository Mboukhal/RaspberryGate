import asyncio
import websockets
import json
import random
import string
from collections import defaultdict

# Dictionary to manage rooms and clients
rooms = defaultdict(set)

# Function to generate random badge data
def generate_random_data():
    badge_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random badge-id
    status = random.choice([True, False])  # Random status (True/False)
    
    return {"data": [{"badge-id": badge_id, "status": status}]}

# Function to send random JSON data to all clients in a room
async def broadcast_to_room(room_name):
    if room_name in rooms and rooms[room_name]:  # Only broadcast if the room has clients
        random_data = generate_random_data()
        json_data = json.dumps(random_data)

        # Send data to all clients in the room
        clients_to_remove = []
        for client in rooms[room_name]:
            if client.open:  # Check if the connection is still open
                try:
                    await client.send(json_data)
                except websockets.ConnectionClosedOK:
                    # Graceful closure, mark the client for removal
                    clients_to_remove.append(client)
            else:
                clients_to_remove.append(client)

        # Remove any clients that have closed connections
        for client in clients_to_remove:
            rooms[room_name].remove(client)
        print(f"Sent to room {room_name}: {json_data}")

# Handler for new WebSocket connections
async def handler(websocket, path):
    try:
        # Server-side logic to assign room
        room_name = "room0"  # You can change this logic to dynamically assign room names
        print(f"Assigning client to room: {room_name}")

        # Add the client to the specified room
        rooms[room_name].add(websocket)
        print(f"Client connected to room: {room_name}")

        # Keep sending random data to the clients in the room every 3 seconds
        while websocket.open:
            await broadcast_to_room(room_name)
            await asyncio.sleep(3)  # Broadcast every 3 seconds
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected from room: {room_name}")
    finally:
        # Remove the client from the room when disconnected
        rooms[room_name].remove(websocket)
        if not rooms[room_name]:  # If room is empty, delete it
            del rooms[room_name]

async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
