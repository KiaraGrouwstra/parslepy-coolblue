"""parse jl"""
import json
import yaml
from argparse import ArgumentParser, FileType
from toolz.curried import pipe

class JLHandler(object):
    """ parse jl"""
    def __init__(self):
        """ parse jl"""
        parser = ArgumentParser(description='process .jl file')
        parser.add_argument('-o', '--output', type=FileType('wb', 0), help='output file, stdout: -')
        parser.add_argument('-i', '--input', type=FileType('r'), help='input file')
        self.cli_args(parser)
        self.args = parser.parse_args()

    def run(self):
        """ iterate over jl lines"""
        # line = self.args.input.readline()
        for line in self.args.input:
            # json.dumps
            # yaml.dump
            # lambda s: json.dumps(s, sort_keys=True, indent=4)
            lien = pipe(line, json.loads, self.fun, json.dumps)
            # print lien
            self.args.output.write(lien + '\n')

    def cli_args(self, parser):
        """ pass handler-specific arguments"""
        pass

    def fun(self, dic):
        """ some function"""
        return dic

if __name__ == '__main__':
    JLHandler().run()
