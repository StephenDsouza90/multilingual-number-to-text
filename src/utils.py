from functools import wraps

from src.models import NumberToTextRequest
from fastapi import HTTPException
from config.logging_config import setup_logging


def log_request_and_response(func):
    """
    Decorator to log request and response for FastAPI endpoints.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: NumberToTextRequest = kwargs.get("request")
        logger = setup_logging()
        if request:
            logger.info(
                {
                    "event": "request_received",
                    "number": request.number,
                    "language": request.language,
                }
            )
        try:
            response = await func(*args, **kwargs)
            logger.info({"event": "response_success", "response": response})
            return response
        except NotImplementedError:
            logger.error(
                {
                    "event": "error",
                    "error": f"Language '{request.language}' is not supported.",
                }
            )
            raise HTTPException(
                status_code=400,
                detail=f"Language '{request.language}' is not supported.",
            )
        except ValueError as ve:
            logger.error(
                {
                    "event": "error",
                    "error": str(ve),
                }
            )
            raise HTTPException(
                status_code=422,
                detail=f"Unprocessable Entity: {str(ve)}",
            )
        except Exception as e:
            logger.error({"event": "error", "error": str(e)})
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    return wrapper
