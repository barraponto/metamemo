from contextlib import contextmanager
from tempfile import TemporaryFile

import requests


@contextmanager
def streaming_download(url):
    """Stream download to temporary file, make it available as a context manager."""
    with requests.get(url, stream=True) as response, TemporaryFile() as tempfile:
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=8 * 2**10):
            tempfile.write(chunk)

        tempfile.seek(0)

        yield tempfile
