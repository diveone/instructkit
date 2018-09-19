import logging


class LogMuter(logging.Filter):
    """
    Mutes loggers by setting their level ot WARN by default.
    """
    def __init__(self, loggers: list, mute_level=logging.WARN):
        self.mute_level = mute_level
        self.loggers = {}
        for log in loggers:
            self.loggers[log] = log.level

    def mute(self):
        for log in self.loggers:
            log.setLevel(self.mute_level)

    def restore(self):
        for log, level in self.loggers.items():
            log.setLevel(level)


class LogMuterTestMixin:
    log_names = []

    def setUp(self):
        super().setUp()
        self.log_muter = LogMuter(self.log_names)
        self.log_muter.mute()

    def tearDown(self):
        self.log_muter.restore()
        super().tearDown()
