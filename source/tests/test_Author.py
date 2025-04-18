import pytest

from ..main.Author import HandlerAuthor

@pytest.fixture
def logs_wo_request():
	return [
		"2025-03-28 12:24:19,000 DEBUG django.db.backends: (0.13) SELECT * FROM 'orders' WHERE id = 60;",
		"2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected",
		"2025-03-28 12:49:16,000 WARNING django.security: SuspiciousOperation: Invalid HTTP_HOST header"
	]

@pytest.fixture
def def_logs():
	return [
		"2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]",
		"2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected",
		"2025-03-28 12:03:09,000 DEBUG django.db.backends: (0.19) SELECT * FROM 'users' WHERE id = 32;",
		"2025-03-28 12:49:16,000 WARNING django.security: SuspiciousOperation: Invalid HTTP_HOST header"
	]


def test_no_request_logs(logs_wo_request):
	with pytest.raises(TypeError) as e:
		author = HandlerAuthor(logs_wo_request)
		author.create()

	assert str(e.value) == "No value to display"

def test_def(def_logs):
	author = HandlerAuthor(def_logs)
	report = author.create()

	assert [
		report.handlers,
		report.debug,
		report.info,
		report.warning,
		report.error,
		report.critical,
		report.total
	] == [
		["/admin/dashboard/"],
		[0],
		[1],
		[0],
		[0],
		[0],
		1
	]