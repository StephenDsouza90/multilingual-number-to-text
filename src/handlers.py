from num2words import num2words

def convert_number_to_text_logic(number: float, language: str, currency: str) -> str:
    """
    Convert a number to its text representation in the specified language.

    Args:
        number (float): The number to be converted.
        language (str): The language code for the conversion (e.g., 'en', 'es', 'fr').
        currency (str): The currency code for the conversion (e.g., 'USD', 'EUR', 'JPY').

    Returns:
        str: The text representation of the number.

    Raises:
        ValueError: If the language is not supported or an error occurs during conversion.
    """
    # Split the number into integer and fractional parts
    # integer_part = int(number)
    # fractional_part = round(number % 1, 2) * 100

    # Convert the integer part to words
    text = num2words(number, lang=language, to="currency", currency=currency)

    # Handle the fractional part with language-specific formatting
    # if fractional_part == 0:
    #     number_text = f"{integer_text}"
    # else:
    #     fractional_text = num2words(int(fractional_part), lang=language)
    #     if language == "en":
    #         number_text = f"{integer_text} and {fractional_text}"
    #     elif language == "fr":
    #         number_text = f"{integer_text} et {fractional_text} centimes"
    #     elif language == "es":
    #         number_text = f"{integer_text} y {fractional_text} centavos"
    #     elif language == "de":
    #         number_text = f"{integer_text} und {fractional_text} Cent"
    #     else:
    #         # Fallback to English if the language is not supported
    #         number_text = f"{integer_text} and {fractional_text} cents"

    return text