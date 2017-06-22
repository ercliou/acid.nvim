from acid.handlers import BaseHandler
from acid.nvim.log import echo_warning

class Handler(BaseHandler):

    name = "MvSingle"
    priority = 0

    def on_init(self):
        self.value = []

    def on_handle(self, msg, *_):
        if 'error' in msg:
            echo_warning(self.nvim, msg['error'])
        else:
            path = msg['touched'][0]
            self.nvim.call('edit', path)
