from acid.commands import BaseCommand
from acid.nvim import current_path
from acid.nvim.log import warning
import os


def ns_to_path(ns):
    return ns.replace("-", "_").replace(".", "/")


class Command(BaseCommand):

    name = 'NewFile'
    priority = 0
    nargs=1
    cmd_name = 'AcidNewFile'
    handlers = {'Ignore': '', 'DoAutocmd': 'AcidRequired'}
    op = "eval"
    mapping = '<leader>N'

    def prepare_payload(self, ns):
        path = os.path.join(current_path(neovim), 'src', ns_to_path(ns))

        with open(path, 'w') as fpath:
            fpath.write('(ns {})'.format(ns))

        self.nvim.nvim_command('silent edit {}'.format(path))

        return {"code": "(require '[{}])".format(ns)}


