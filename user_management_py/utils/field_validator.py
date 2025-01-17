"""Docstring."""

import re


def validate_email(email: str) -> bool:
    """Validate the given email address.

    Parameters
    ----------
    email : str
        The email address to be validated.

    Returns
    -------
    bool
        Returns `True` if the email is valid, otherwise returns `False`.
    """
    email_pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None


def validate_password(password: str) -> tuple[bool, str]:
    """Validate the given password.

    Parameters
    ----------
    password : str
        Password to be validated.

    Returns
    -------
    tuple[bool, str]
        Returns `True` if password is valid, otherwise returns `False` and
        the reason why the password is not valid.
    """
    if len(password) <= 8 or len(password) >= 32:
        return False, "Password must be between 8 and 32 characters long."
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search("[!@#$%^&*()_+]", password):
        return False, "Password must contain at least one special character."
    return True, ""
