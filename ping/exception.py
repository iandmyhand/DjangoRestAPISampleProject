from www.exception.exception_base import ExceptionBase


class SampleException(ExceptionBase):

    def __init__(self, code, status=None, data=None, message_data=None, *args, **kwargs):
        super(SampleException, self).__init__(code=code, status=status, data=data,
                                              message_data=message_data, *args, **kwargs)
