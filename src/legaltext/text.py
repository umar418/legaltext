import re


def normalize_white_space(text: str) -> str:
    """
    Normalize white space in a string by replacing multiple spaces with a single space
    and stripping leading/trailing spaces.

    Args:
        text (str): The input string to normalize.

    Returns:
        str: The normalized string with single spaces and no leading/trailing spaces.
    """
    # Replace multiple whitespace characters with a single space
    normalized_text = re.sub(r"\s+", " ", text)
    # Strip leading and trailing whitespace
    return normalized_text.strip()
