from twttr import shorten


def test_shorten():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"
    assert shorten("h@llo w*Orld!!!") == "h@ll w*rld!!!"
