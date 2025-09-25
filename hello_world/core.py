"""
Core functionality for the hello world package.
"""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    
    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Python")
        'Hello, Python!'
    """
    # TODO: Trigger comment via the workflow!

    return f"Hello, {name}!"


def farewell(name: str = "World") -> str:
    """
    Generate a farewell message.
    
    Args:
        name (str): The name to bid farewell to. Defaults to "World".
    
    Returns:
        str: A farewell message.
    
    Examples:
        >>> farewell()
        'Goodbye, World!'
        >>> farewell("Python")
        'Goodbye, Python!'
    """
    return f"Goodbye, {name}!"
