from longest_common_prefix import lcp


def test_lcp():
    assert lcp(["flower","flow","flight"]) == "fl"
    