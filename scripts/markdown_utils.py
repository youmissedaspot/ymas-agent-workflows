"""Small shared parser for visible Markdown lines, excluding fenced examples."""

import re


def visible_lines(contents):
    fence_char = None
    fence_size = 0
    fence_quote_depth = 0
    for line in contents.splitlines():
        content = line
        quote_depth = 0
        while match := re.match(r"^ {0,3}>[ \t]?", content):
            quote_depth += 1
            content = content[match.end():]
        # A quoted fenced block ends with its quote container.
        if fence_char is not None and quote_depth < fence_quote_depth:
            fence_char = None
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", content)
        if fence_char is not None:
            if marker and quote_depth == fence_quote_depth and marker[1][0] == fence_char and len(marker[1]) >= fence_size and not marker[2].strip():
                fence_char = None
            continue
        if marker:
            fence_char, fence_size = marker[1][0], len(marker[1])
            fence_quote_depth = quote_depth
            continue
        yield line


def without_inline_code(line):
    """Remove code spans closed by the same length backtick run as the opener."""
    markers = list(re.finditer(r"`+", line))
    result = []
    cursor = 0
    index = 0
    while index < len(markers):
        opening = markers[index]
        closing = next((i for i in range(index + 1, len(markers))
                        if len(markers[i][0]) == len(opening[0])), None)
        if closing is None:
            index += 1
            continue
        result.append(line[cursor:opening.start()])
        cursor = markers[closing].end()
        index = closing + 1
    result.append(line[cursor:])
    return "".join(result)
