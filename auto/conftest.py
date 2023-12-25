import pytest
@pytest.fixture(dcope = 'session', autouse = True)
def exe_sql():
    print('请求之前')
    yield
    print('请求之后')