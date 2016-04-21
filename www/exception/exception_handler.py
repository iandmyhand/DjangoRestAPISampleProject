import logging
import sys
import traceback

from www.exception.response import JsonErrorResponse
from www.exception.exception_base import ExceptionBase

logger = logging.getLogger('www.custom')


class CustomExceptionHandler:

    def process_exception(self, request, exception):

        _type, _value, _traceback = sys.exc_info()
        _formatted_traceback = ''.join(str(entry) for entry in traceback.format_tb(_traceback, limit=10))
        logger.error(_formatted_traceback)
        logger.error('Request: %s' % str(request))
        logger.error('Exception type: %s' % _type)
        logger.error('Exception value: %s' % _value)
        logger.error(str('Exception items: ' + ', '.join('%s: %s' % item for item in vars(exception).items())))

        if hasattr(exception, 'code'):
            _code = exception.code
        else:
            _code = None

        if hasattr(exception, 'status'):
            _status = exception.status
        else:
            _status = None

        if hasattr(exception, 'data'):
            _data = exception.data
        else:
            _data = None

        if hasattr(exception, 'message_data'):
            _message_data = exception.message_data
        else:
            _message_data = None

        if isinstance(exception, ExceptionBase) or 'application/json' == request.META.get('CONTENT_TYPE', None):
            return JsonErrorResponse(code=_code, status=_status, data=_data, message_data=_message_data)

        logger.error('This exception is not a instance of ExceptionBase!!!')
        raise exception


def page_not_found(request, *args, **kwargs):
    logger.warn('Page not found!!!')
    for _meta in request.META:
        logger.warn('%s: %s' % (_meta, request.META[_meta]))
    return JsonErrorResponse('PAGE_NOT_FOUND')


def server_error(request, *args, **kwargs):
    logger.error('Server error occurred!!!')
    for _meta in request.META:
        logger.error('%s: %s' % (_meta, request.META[_meta]))
    return JsonErrorResponse('UNKNOWN_ERROR')
