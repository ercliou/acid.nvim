from acid.commands import BaseCommand
from acid.nvim import current_file, current_path
import os


class Command(BaseCommand):

    name = 'Rename'
    priority = 0
    nargs = 1
    cmd_name = 'AcidRename'
    handlers = ['Echo']
    prompt = 1
    op = "rename-file-or-dir"

    def prepare_payload(self, path):
        current = current_file(self.nvim)
        root = current_path()
        final = os.path.join(root, 'src', *path.replace('-', '_').split('.'))
        return {"old-path": current, "new-path": final}

