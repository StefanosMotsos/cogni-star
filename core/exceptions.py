import logging

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        return response

    logger.exception("Unhandled exception in view", exc_info=exc)

    return Response(
        {"detail": "An unexpected error occurred."},
        status=500,
    )