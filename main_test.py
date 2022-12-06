from main import start


def test_main_pytest():
    start_resp = start()
    assert start_resp != 123
