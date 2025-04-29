from fastapi import FastAPI
from num2words import num2words

from src.models import NumberToTextRequest
from src.utils import log_request_and_response


# Create a FastAPI instance
app = FastAPI()


@app.post("/convert")
@log_request_and_response
async def convert_number_to_text(request: NumberToTextRequest):
    """
    Convert a number to its text representation in the specified language.

    Args:
        request (NumberToTextRequest): The request object containing the number and language.

    Returns:
        dict: A dictionary containing the original number, its text representation, and the language used.

    Raises:
        HTTPException: If the language is not supported or an error occurs during conversion.
    """
    # Split the number into integer and fractional parts
    integer_part = int(request.number)
    fractional_part = round(request.number % 1, 2) * 100

    # Convert the integer part to words
    integer_text = num2words(integer_part, lang=request.language)

    # Handle the fractional part with language-specific formatting
    if fractional_part == 0:
        number_text = f"{integer_text}"
    else:
        fractional_text = num2words(int(fractional_part), lang=request.language)
        if request.language == "en":
            number_text = f"{integer_text} and {fractional_text} cents"
        elif request.language == "fr":
            number_text = f"{integer_text} et {fractional_text} centimes"
        elif request.language == "es":
            number_text = f"{integer_text} y {fractional_text} centavos"
        elif request.language == "de":
            number_text = f"{integer_text} und {fractional_text} Cent"
        else:
            # Fallback to English if the language is not supported
            number_text = f"{integer_text} and {fractional_text} cents"

    return {"number": request.number, "text": number_text, "language": request.language}
