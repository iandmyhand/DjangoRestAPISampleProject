import logging

from rest_framework.views import APIView

from www.response import SuccessResponse

from ping.exception import SampleException

logger = logging.getLogger('www.custom')


class IndexViewSet(APIView):

    def get(self, request):
        for _meta in request.META:
            logger.info('%s: %s' % (_meta, request.META[_meta]))
        return SuccessResponse(None)


class ExceptionViewSet(APIView):

    def get(self, request):
        logger.error('exception test!')
        raise SampleException('SAMPLE', message_data={'name': 'test'})
