ENCODING = "utf-8"


async def build_headers_map(b_headers: List[bytes]):
    def str_encode(b_items):
        return [b_item.strip().decode(ENCODING) for b_item in b_items]

    return {
        items[0].lower(): items[1]
        for items in [str_encode(b_header.split(b":")) for b_header in b_headers]
    }


async def parse_request(reader) -> Tuple[str, dict, str]:
    b_request = await reader.readline()

    b_headers: List[bytes] = []

    while True:
        b_line = await reader.readline()
        if b_line == b"\r\n":
            break
        b_headers.append(b_line)

    headers_map = await build_headers_map(b_headers)

    content_length = int(headers_map.get("content-length", 0))

    b_body = await reader.read(content_length) if content_length > 0 else b""

    return (
        b_request.decode(ENCODING),
        headers_map,
        b_body.decode(ENCODING) if b_body else None,
    )
