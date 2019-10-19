import logging
import argparse
import sys

from helpers.cli_helpers import *

class Cli(object):

    @classmethod
    def parse(cls, args):
        parser = argparse.ArgumentParser(description="Birbal Question Generator", add_help=False)
        sub_parsers = parser.add_subparsers()

        topic_parser = sub_parsers.add_parser("topics", help="Keywords that represents the topic")
        topic_parser.add_argument("-k", "--keywords", help="Comma separated list of keywords [max 3]")

        question_parser = sub_parsers.add_parser("questions", help="Questions from the tags")
        question_parser.add_argument("-k", "--tags", help="Comma separated list of tags  \
                                                [returns max 1000 questions for each tag]")

        args = parser.parse_args()

        helpers = Helpers()

        try:
            if args.cmd == "topics":
                return helpers.fetch_topics(args.keywords)
            elif args.cmd == "questions":
                return helpers.fetch_questions(args.topics)
        finally:
            logging.debug("Cleaning up")



def main():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    Cli.parse()

    sys.exit(ret_code)
