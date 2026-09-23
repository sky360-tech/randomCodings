
# Updated at 2026-09-23T19:36:40.186889
def calculate_sha256(data: bytes) -> str:
    import hashlib
    return hashlib.sha256(data).hexdigest()

