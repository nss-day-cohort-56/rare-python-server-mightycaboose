import sqlite3
import json
from models import Post, User, Category

def get_all_posts():
    """method to retrieve posts with """
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name user_first_name,
            u.last_name user_last_name,
            c.label category_label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        LEFT JOIN Categories c
            ON c.id = p.category_id
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post = Post(row['id'], row['user_id'], row['category_id'], 
                            row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            user = User(row['id'], row['user_first_name'], row['user_last_name'], '', '', '', '', '', '', '')

            category = Category(row['id'], row['category_label'] )

            post.user = user.__dict__

            post.category = category.__dict__
            
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_posts_by_user_id(user_id):
    """ please"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name user_first_name,
            u.last_name user_last_name,
            c.label category_label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        LEFT JOIN Categories c
            ON c.id = p.category_id
        WHERE user_id = ?
        """, (user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                            row['publication_date'], row['image_url'], row['content'], row['approved'])
            user = User(row['id'], row['user_first_name'], row['user_last_name'], '', '', '', '', '', '', '')

            category = Category(row['id'], row['category_label'] )

            post.user = user.__dict__

            post.category = category.__dict__
            
            posts.append(post.__dict__)

    return json.dumps(posts)


def get_single_post(id):
    """get single post"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url  user_profile_image_url,
            u.created_on  user_created_on,
            u.active user_active
        FROM Posts p
        JOIN Users u
            on u.id = p.user_id
        WHERE p.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        post = Post(data['id'],
                    data['user_id'],
                    data['category_id'],
                    data['title'],
                    data['publication_date'],
                    data['image_url'],
                    data['content'],
                    data['approved'])

        user = User(
            data['user_id'],
            data['user_first_name'],
            data['user_last_name'],
            data['user_email'],
            data['user_bio'],
            data['user_username'],
            data['user_password'],
            data['user_profile_image_url'],
            data['user_created_on'],
            data['user_active']
        )

        post.user = user.__dict__

        return json.dumps(post.__dict__)
