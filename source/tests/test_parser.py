from .parser_fixtures import *

from ..services.Parser import ArgvParser

parser_to_test = ArgvParser()


def test_normal(normal_args):
	parsed_args = parser_to_test.get_parsed_argv(
		normal_args
	)
	expected =  (
		[
			"logs/log1.log",
			"logs/log2.log"
		],
		[],
		{}
	)
	assert parsed_args == expected

def test_empty_args(empty_args):
	with pytest.raises(TypeError) as e:
		parsed_args = parser_to_test.get_parsed_argv(
			empty_args
		)
	assert str(e.value) == "empty argv list"

def test_empty():
	with pytest.raises(TypeError) as e:
		parsed_args = parser_to_test.get_parsed_argv(

		)

	assert str(e.value) == "Argv is not defined"
def test_normal_with_flags(args_with_flags):
	parsed_args = parser_to_test.get_parsed_argv(
		args_with_flags
	)
	expected = (
		[
			"logs/log1.log",
			"logs/log2.log"
		],
		[],
		{"--report": "handler"}
	)

	assert parsed_args == expected

def test_raise_no_value_after_long_flag_error(no_arg_after_long_flag, two_long_flags_in_row):
	with pytest.raises(TypeError) as e:
		parsed_args = parser_to_test.get_parsed_argv(
			no_arg_after_long_flag
		)

	with pytest.raises(TypeError) as e2:
		parsed_args = parser_to_test.get_parsed_argv(
			two_long_flags_in_row
		)

	assert "positional argument expected after" in str(e.value)
	assert "positional argument expected after" in str(e2.value)

def test_raise_not_expected_flag(short_unexpected_flag, long_unexpected_flag):
	with pytest.raises(TypeError) as unexp_long_flag_error:
		parsed_args = parser_to_test.get_parsed_argv(
			long_unexpected_flag
		)

	with pytest.raises(TypeError) as unexp_short_flag_error:
		parsed_args = parser_to_test.get_parsed_argv(
			short_unexpected_flag
		)

	expected = "is not expected flag"

	assert expected in str(unexp_long_flag_error.value)
	assert expected in str(unexp_short_flag_error.value)

def test_unexpected_file_extension(unexpected_file_extension):
	with pytest.raises(TypeError) as err:
		parsed_args = parser_to_test.get_parsed_argv(
			unexpected_file_extension
		)

	assert str(err.value) == "The extension of the transferred file is not expected."