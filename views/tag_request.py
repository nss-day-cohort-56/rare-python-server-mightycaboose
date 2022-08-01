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
        ORDER BY t.label
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
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'],))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Hannah said I didn't need the additional lines of codes, deleted it

    return json.dumps(new_tag)

def delete_tag(id):
    """Function to delete category from database that matches id given as argument
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Tags
        WHERE id = ?
        """, (id, ))

def update_tag(id, new_tag):
    """update name of category"""

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Tags
            SET
                label = ?
        WHERE id = ?
        """, (new_tag['label'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
