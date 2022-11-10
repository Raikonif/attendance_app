import pytest
from src.helpers import  discover_data_files, read_file


def test_discover_data_files():
    files = discover_data_files()
    assert files is not None, 'Should be non-null result'
    assert type(files) is list, 'Should be a list instance'

def test_discover_data_files_fake_path():
    fake_path = "fake_path"
    with pytest.raises(expected_exception=FileNotFoundError):
        discover_data_files(fake_path)

def test_read_file():
    data = read_file(["../data/Practice Modulo 1 - Grupo 4 - Attendance report 10-10-22 (1).csv"])
    assert data is not None
    assert type(data) is list
    assert all(type(d[0]) is str for d in data)
    assert all(hasattr(d[1], '__iter__') for d in data)

def test_read_data_fake_path():
    fake_path = "fake_path"
    with pytest.raises(expected_exception=FileNotFoundError):
        read_file(fake_path)
