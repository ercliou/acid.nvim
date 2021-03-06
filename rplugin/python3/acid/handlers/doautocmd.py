from acid.handlers import BaseHandler


class Handler(BaseHandler):

    name = "DoAutocmd"
    priority = 0

    def on_init(self):
        self.cmd_group = ""
        self.successful = True

    def configure(self, cmd_group, *args, **kwargs):
        super().configure(*args, **kwargs)
        self.cmd_group = cmd_group
        return self

    def on_handle(self, msg, *_):
        self.successful = self.successful and not 'err' in msg

    def on_after_finish(self, *_):
        if self.successful:
            self.nvim.command("doautocmd User {}".format(self.cmd_group))

