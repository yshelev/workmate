import sys

from source.main.Author import HandlerAuthor
from source.services.FileWorker import FileWorker
from source.services.Parser import ArgvParser
from source.services.Printer import PrinterHandler


def main():
	parser = ArgvParser()

	parser.set_argv(sys.argv)
	paths, short_flags, long_flags = parser.get_parsed_argv()

	data = FileWorker(paths).get_lines_from_files()
	report = HandlerAuthor(data).create()

	PrinterHandler(report).print()

if __name__ == "__main__":
	main()