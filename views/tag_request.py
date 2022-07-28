import sqlite3
import json
from models import Tag

def get_all_tags():
    """Get all tags"""
    #Open a connection to database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query
        # Parameters must match in exact order
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
            
        FROM Tags t
        """)

        # Initialize an empty list
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate through the list of data returned from database
        for row in dataset:

            # Create a new instance from current row. Must match SQL format.
            tag = Tag(row ['id'], row['label'])

            tags.append(tag.__dict__)
    
    # Serialize list as JSON
    return json.dumps(tags)

def create_tag(new_tag):
    """"Function that adds a new tag to the list
    Args:
        Tag(dict): The new tag to be added
    Returns:
        dict: The tag that was added with its new id
    """""
    with sqlite3.connect("./db.sqlite3.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'],))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_tag['id'] = id
        for tag in new_entry['tags']:
            
            db_cursor.execute("""
            INSERT INTO EntryTag
                ( entry_id, tag_id ) 
            VALUES
                ( ?, ?);
            """, (id, tag))

    return json.dumps(new_entry)