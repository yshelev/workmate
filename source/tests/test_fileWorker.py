import pytest

from ..services.FileWorker import FileWorker

@pytest.fixture
def not_existed_file():
	return ["logs/nexisted.log"]

@pytest.fixture
def empty_file():
	return ["logs/empty.log"]

@pytest.fixture
def one_file():
	return ["logs/def_log1.log"]

@pytest.fixture
def many_files():
	return [
		"logs/def_log1.log",
		"logs/def_log2.log"
	]

def test_empty_file(empty_file):
	lines = FileWorker(empty_file).get_lines_from_files()

	assert lines == []

def test_one_file(one_file):
	lines = FileWorker(one_file).get_lines_from_files()

	assert lines == [
		"2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]",
		"2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected"
	]

def test_many_files(many_files):
	lines = FileWorker(many_files).get_lines_from_files()

	assert lines == [
		"2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]",
		"2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected",
		"2025-03-28 12:03:09,000 DEBUG django.db.backends: (0.19) SELECT * FROM 'users' WHERE id = 32;",
		"2025-03-28 12:05:13,000 INFO django.request: GET /api/v1/reviews/ 201 OK [192.168.1.97]"
	]

def test_not_existed_file(not_existed_file):
	with pytest.raises(TypeError) as e:
		lines = FileWorker(not_existed_file).get_lines_from_files()

	assert "doesn't exists" in str(e.value)