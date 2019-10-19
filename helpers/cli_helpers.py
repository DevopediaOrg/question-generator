import operator
from source.stackexchange_api import StackExchange



class CliHelpers(object):

    @classmethod
    def extract_tags_from_stackexchange(keywords):
       api = StackExchange()
       tags_list={}
       for keyword in keywords:
           tags = api.fetch_tags(keyword)
           tags_dict={}

           for tag in tags["items"]:
               tags_dict[tag["name"]]=tag["count"]

           sorted_tags = sorted(tags_dict.items(), key=operator.itemgetter(0),reverse=True)
           tags_list[keyword] = map(lambda s: s[1], sorted_tags)

        return tags_list
