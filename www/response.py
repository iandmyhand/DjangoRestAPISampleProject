from rest_framework.response import Response


class DefaultResponse(Response):

    def __init__(self, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):

        super(DefaultResponse, self).__init__(
            data=self.data,
            status=status,
            template_name=template_name, headers=headers,
            exception=exception, content_type=content_type)


class SuccessResponse(DefaultResponse):

    def __init__(self, data=None, code=None, message=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        self.code = code if code else 0
        self.message = message if message else 'OK'
        self.data = {
            'message': self.message,
            'code': self.code,
        }
        if data:
            self.data['data'] = data
        super(SuccessResponse, self).__init__(
            # data=self.data,
            status=status,
            template_name=template_name, headers=headers,
            exception=exception, content_type=content_type)
