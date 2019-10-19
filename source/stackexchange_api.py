from ..helpers.apis import Api

class StackExchange(object):

    def __init__(self, min=100, order='votes'):
        self.source = "stackoverflow"
        self.api = Api.get_instance(self.source)
        self.min = min
        self.order = order

    def fetch_tags(self, keyword):
        return self.api.fetch('tags', inname=keyword, min=100)


    def fetch_questions(self, from_date, to_date, tag, min=20, sort='votes'):
        return self.api.fetch('questions', from_date, to_date, min=min, tagged=tag, sort=sort)


    def fetch_answers(self, ids=[]):
        return self.api.fetch('answers', ids=ids)


    def fetch_users(self, ids=[]):
        return self.api.fetch('users', ids=ids)
