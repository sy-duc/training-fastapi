import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger()

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)        
        log_dict = {
            "url": request.url.path,
            "method": request.method,
            "process_time": time.time() - start_time
        }
        logger.info(log_dict)
        return response
