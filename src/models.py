from pydantic import BaseModel


class NumberToTextRequest(BaseModel):
    """
    Request model for converting a number to its text representation.

    Attributes:
        number (float): The number to be converted.
        language (str): The language code for the conversion (e.g., 'en', 'es', 'fr').
        currency (str): The currency code for the conversion (e.g., 'USD', 'EUR', 'JPY').
    """

    number: float
    language: str
    currency: str
