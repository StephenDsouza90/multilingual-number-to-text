from pydantic import BaseModel


class NumberToTextRequest(BaseModel):
    """
    Request model for converting a number to its text representation.

    Attributes:
        number (float): The number to be converted.
        language (str): The language code for the conversion (e.g., 'en', 'es', 'fr').
    """

    number: float
    language: str
