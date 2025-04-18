import pytest


@pytest.fixture
def long_flag_wo_arg():
	return ["main.py", "logs/log1.log", "logs/log2.log", "--report", "handler"]

@pytest.fixture
def normal_args():
	return ["main.py", "logs/log1.log", "logs/log2.log"]

@pytest.fixture
def empty_args():
	return ["main.py"]

@pytest.fixture
def args_with_flags():
	return ["main.py", "logs/log1.log", "logs/log2.log", "--report", "handler"]

@pytest.fixture
def no_arg_after_long_flag():
	return ["main.py", "logs/log1.log", "logs/log2.log", "--report"]

@pytest.fixture
def short_unexpected_flag():
	return ["main.py", "logs/log1.log", "-a"]

@pytest.fixture
def long_unexpected_flag():
	return ["main.py", "logs/log1.log", "--flush"]

@pytest.fixture
def two_long_flags_in_row():
	return ["main.py", "logs/log1.log", "--report", "--report"]

@pytest.fixture
def unexpected_file_extension():
	return ["main.py", "logs/log1.lg", "--report"]
