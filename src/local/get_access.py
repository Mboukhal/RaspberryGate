import sqlite3, os
import inspect


CONN = None

file_path = inspect.getfile(inspect.currentframe())
current_dir = os.path.dirname(os.path.abspath(file_path))
DB_FILE = os.path.join(current_dir, 'badges.db')

# Function to check access for a given badgeId from SQLite database
def get_access(badge_id):
    
    global CONN
    
    if not os.path.exists(DB_FILE):
        return {"ok": False, "message": "Database not found."}
      
    try:
      if not CONN:
        CONN = sqlite3.connect(DB_FILE)
    
      cursor = CONN.cursor()
      cursor.execute('SELECT 1 FROM badges WHERE badge_id = ?', (badge_id,))
      result = cursor.fetchone()
    
      return {"ok": result is not None, "message": "Badge database."}
    
    except Exception as e:
      if CONN:
        CONN.close()
        CONN = None
     
      return {"ok": False, "message": "Database error: " + str(e)}
 