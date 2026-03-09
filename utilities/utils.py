def clean_text(text: str, keep_spaces: bool = True, allowedChars: list[str] | None = None) -> str:
    output_str: str = ''
    for char in text:
        if char.isalpha() or (char == ' ' and keep_spaces) or (allowedChars and char in allowedChars):
            output_str += char
    return output_str
