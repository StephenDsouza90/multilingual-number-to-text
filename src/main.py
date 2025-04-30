from fastapi import FastAPI

from src.models import NumberToTextRequest
from src.utils import log_request_and_response
from src.handlers import convert_number_to_text_logic

# Create a FastAPI instance
app = FastAPI()


@app.post("/convert")
@log_request_and_response
async def convert_number_to_text(request: NumberToTextRequest):
    """
    API endpoint to convert a number to its text representation in the specified language.

    Args:
        request (NumberToTextRequest): The request object containing the number and language.

    Returns:
        dict: A dictionary containing the original number, its text representation, and the language used.
    """
    number_text = convert_number_to_text_logic(request.number, request.language)
    return {"number": request.number, "text": number_text, "language": request.language}
