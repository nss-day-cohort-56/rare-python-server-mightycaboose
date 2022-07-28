class Post():
    """creates Post dictionary
    """

    def __init__(self, id, user_id, category, title, publication_date, image_url, content, approved):
        self.id = id
        self.user_id = user_id
        self.category = category
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
        