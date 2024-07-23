def get_secret(name):
    """
    Get the secret string from the first line of the specified file.

    Args:
    name (str): The name of the file (without the .txt extension).

    Returns:
    str: The secret string from the first line of the file.
    """
    try:
        with open(f'../secrets/{name}.txt', 'r') as file:
            secret = file.readline().strip()
        return secret
    except FileNotFoundError:
        return f"Error: The file ../secrets/{name}.txt does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
