from enum import Enum

import from stackapi import StackAPI


class Api(object):
    __instance = {}

    def __init__(self, source):
      """ Virtually private constructor. """
      if Api.__instance[source] != None:
         raise Exception("This class is a singleton!")
      else:
         Api.__instance[source] = get_instance(source)


    @staticmethod
    def get_instance(source):
        if Api.__instance[source] == None:
            if __Api[source] == __API.stackoverflow:
                return StackAPI('stackoverflow')

        return Api.__instance[source]


class __API(Enum):
    stackoverflow = "stackoverflow"

    def __str__(self):
        return self.value
