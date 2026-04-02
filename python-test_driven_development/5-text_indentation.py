#!/usr/bin/python3
"""This module defines a function that prints text with indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    new_text = ""

    while i < len(text):
        char = text[i]

        new_text += char

        if char in ".?:":
            new_text += "\n\n"

            # skip spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    # print lines without leading/trailing spaces
    lines = new_text.split("\n")
    for line in lines:
        print(line.strip())
