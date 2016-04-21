import logging

logger = logging.getLogger('www.custom')


class ExceptionBase(Exception):

    code = None
    status = None
    data = None
    message_data = None

    def __init__(self, code, status=None, data=None, message_data=None, *args, **kwargs):
        self.code = code
        self.status = status
        self.data = data
        self.message_data = message_data
        super(ExceptionBase, self).__init__(code, status, data, message_data, *args, **kwargs)
