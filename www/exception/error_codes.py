from django.utils.translation import ugettext_lazy as _

ERROR_CODES = {
    'SAMPLE': {
        'status': 400,
        'code': 1000,
        'message': _('SAMPLE_%(name)s_EXCEPTION'),
    },

    'PAGE_NOT_FOUND': {
        'status': 404,
        'code': 9001,
        'message': _('PAGE_NOT_FOUND'),
    },
    'SHOULD_BE_AJAX': {
        'status': 400,
        'code': 9002,
        'message': _('SHOULD_BE_AJAX'),
    },
    'FAILED_TO_CONNECT_EXTERNAL_API': {
        'status': 500,
        'code': 9003,
        'message': _('FAILED_TO_CONNECT_EXTERNAL_API'),
    },
    'UNKNOWN_ERROR': {
        'status': 500,
        'code': 9999,
        'message': _('UNKNOWN_ERROR'),
    },
}
