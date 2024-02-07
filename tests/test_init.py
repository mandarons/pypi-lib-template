import pytest

import replaceme


@pytest.mark.asyncio
async def test_hello_world():
    assert replaceme.hello_world() == "Hello, World!"
