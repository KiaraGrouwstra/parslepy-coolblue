"""parse jl"""
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import argparse
import json
import yaml
from jl import JLHandler
from parslepy import Parselet
from toolz.curried import pipe, merge
from fp import pick

class ParsleyHandler(JLHandler):
    """ parsley jl"""

    def __init__(self):
        super(ParsleyHandler, self).__init__()
        self.plet = pipe(self.args.parselet.read(), yaml.load, json.dumps, Parselet.from_jsonstring)

    def cli_args(self, parser):
        parser.add_argument('-p', '--parselet', type=argparse.FileType('r'), help='parselet file')

    def fun(self, dic):
        return merge(pick(['_url'], dic), self.plet.parse(StringIO(dic['_body'])))

if __name__ == '__main__':
    ParsleyHandler().run()
