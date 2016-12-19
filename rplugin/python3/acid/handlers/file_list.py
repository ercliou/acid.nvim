from acid.handlers import BaseHandler
from acid.nvim import find_file_in_path
from zen.string import produce_select_options
from zen.ui import selection_window


class Handler(BaseHandler):

    name = "FileList"

    def on_init(self):
        self.acc = {}

    def on_handle(self, msg, *_):
        if 'occurrence' in msg:
            key = msg['occurrence']['name']
            buf_nr = self.nvim.current.buffer.number
            self.acc[key] = ':wincmd p | edit +{} {} | bd {}<CR>'.format(
                msg['occurrence']['line-beg'],
                msg['occurrence']['file'],
                buf_nr
            )

    def after_finish(self):
        selection_window(
            self.nvim,
            header="Select file",
            select_options=produce_select_options(self.acc)
        )
