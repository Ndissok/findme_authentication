import logging
import time

logger = logging.getLogger("django.request")

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = (time.time() - start_time) * 1000  # ms

        logger.info(
            f"{request.method} {request.get_full_path()} "
            f"Status: {response.status_code} "
            f"Duration: {duration:.2f}ms "
            f"User: {getattr(request.user, 'email', 'Anonymous')}"
        )
        return response