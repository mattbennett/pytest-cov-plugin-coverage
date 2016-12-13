from demo.app import foo

pytest_plugins = "pytester"


def test_true(one):
    assert foo(one) is True


def test_false(zero):
    assert foo(zero) is False


def test_with_pytester(testdir):
    # doesn't work either

    testdir.makepyfile(
        """
        from demo.app import foo

        def test_true(one):
            assert foo(one) is True


        def test_false(zero):
            assert foo(zero) is False
        """
    )
    result = testdir.runpytest()
    assert result.ret == 0
