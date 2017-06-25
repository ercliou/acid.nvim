from acid.commands import BaseCommand
from acid.nvim import get_acid_ns


class Command(BaseCommand):

    name = 'ExpandMacro'
    priority = 0
    cmd_name = 'AcidExpandMacro'
    handlers = ['MetaRepl']
    mapping = 'cme'
    shorthand = '''normal! mx$?^(\<lt>CR>\\"sy%`x'''
    opfunc = True
    nargs='*'
    op = "macro-expand"

    def prepare_payload(self, *args):
        return {'code': " ".join(args), }
