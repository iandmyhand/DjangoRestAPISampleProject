import logging

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from www.exception.error_codes import ERROR_CODES
from www.encoder import LazyJSONEncoder

logger = logging.getLogger('www.custom')


class JsonErrorResponse(JsonResponse):

    def __init__(self, code, status=None, data=None, message_data=None, encoder=LazyJSONEncoder, safe=True, **kwargs):
        kwargs.setdefault('content_type', 'application/json')

        if not code:
            code = 'UNKNOWN_ERROR'

        _data = dict()
        _status = None

        if status is not None:
            _status = status

        _error = ERROR_CODES.get(code)
        if _error:
            _data['code'] = _error.get('code', 9999)
            _message = _error.get('message')
            if _message and message_data:
                try:
                    _message = _message % message_data
                except Exception as e:
                    logger.warn('Message not converted with message data.')
                    logger.warn(str(e))
            if not _message:
                _message = _('UNKNOWN_ERROR')
            _data['message'] = _message
            if _status is None:
                _status = _error.get('status', 500)

        if not _data.get('code'):
            _data['code'] = 9999
        if not _data.get('message'):
            _data['message'] = _('UNKNOWN_ERROR')

        if data is not None:
            _data['data'] = data

        if _status is None:
            _status = 500
        kwargs['status'] = _status

        super(JsonErrorResponse, self).__init__(data=_data, encoder=encoder, safe=safe, **kwargs)
