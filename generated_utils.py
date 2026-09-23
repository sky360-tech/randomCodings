
# Updated at 2026-09-23T19:36:40.186889
def calculate_sha256(data: bytes) -> str:
    import hashlib
    return hashlib.sha256(data).hexdigest()


# Updated at 2026-09-23T19:36:40.238317
def sanitize_header(header_val: str) -> str:
    return header_val.replace('\r', '').replace('\n', '')

