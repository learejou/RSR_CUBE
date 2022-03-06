from django.http import Http404


class Post:

    def __init__(self):
        pass

    POSTS = [
        {'id': 1, 'title': 'First', 'body': 'This is my pepe'},
        {'id': 2, 'title': 'Second', 'body': 'This is my pepe'},
        {'id': 3, 'title': 'Third', 'body': 'This is my pepe'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404