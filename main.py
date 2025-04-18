import sys

from source.main.Chooser import Chooser
from source.services.Parser import ArgvParser


def main():
	parser = ArgvParser()

	parser.set_argv(sys.argv)
	paths, short_flags, long_flags = parser.get_parsed_argv()

	Chooser().create(
		paths,
		short_flags,
		long_flags
	)


if __name__ == "__main__":
	main()