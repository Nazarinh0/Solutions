# from solution import MultiKeyDict


def test_multikeydict_access():
    mkd = MultiKeyDict(a=1, b='foo')
    assert mkd['a'] == 1
    assert mkd['b'] == 'foo'

    mkd.alias(aa='a', bb='b')
    assert mkd['aa'] == 1
    assert mkd['bb'] == 'foo'


def test_multikeydict_assignment():
    mkd = MultiKeyDict(x=100, y=[10, 20])

    mkd.alias(z='x')
    mkd['z'] += 1
    assert mkd['x'] == 101

    mkd.alias(z='y')
    mkd['z'] += [30]
    assert mkd['y'] == [10, 20, 30]
    
