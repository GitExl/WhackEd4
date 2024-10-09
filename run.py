from glob import glob
from pathlib import Path

from dehacked.patch.analyzer import Analyzer
from dehacked.patch.parser import Parser
from dehacked.patch.tokenizer import Tokenizer
from dehacked.target import Target
from dehacked.target_loader import TargetLoader

def loads():
    target_loader = TargetLoader(Path('.'), validate_jsonschema=False)
    target_info = target_loader.list_targets()
    option_info = target_loader.list_options()

    # target = Target.from_info_with_options(target_info['mbf'], [
    #     option_info['dehextra'],
    #     option_info['mbf21'],
    #     option_info['dsdhacked'],
    # ])

    analyzer = Analyzer(target_info, option_info)

    for file_path in glob('test_idgames/*'):
        with open(file_path, 'r', encoding='latin1') as f:
            text = f.read()

        tokenizer = Tokenizer(text)
        tokenizer.tokenize()

        parser = Parser(tokenizer.get_tokens())
        parser.parse()

        valid_targets, valid_options, required_options = analyzer.get_valid_targets(parser.get_sections())
        if len(required_options) > 0:
            print(file_path)
            print(valid_targets, valid_options, required_options)
            print()


# import cProfile
# import pstats
# res = cProfile.run('loads()', 'pstats')
# p = pstats.Stats('pstats')
# p.sort_stats(pstats.SortKey.TIME).print_stats(20)

loads()
