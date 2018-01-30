class News:
    """
    News class to define News objects
    """

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Source:
    """
    sources class to define source objects
    """

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

class Category:
    """
    categories class to define category objects
    """

    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
