from source.main.Author import HandlerAuthor
from source.services.FileWorker import FileWorker
from source.services.Printer import PrinterHandler


class Chooser:
	HANDLER = "HANDLER"

	def create(self,
	           paths: list[str],
	           short_flags: list[str],
	           long_flags: dict[str, str]) -> None:
		report_type = long_flags.get("--report", "HANDLER")

		match report_type:
			case self.HANDLER:
				self.__create_handler_report(paths)


	def __create_handler_report(self,
	                            paths: list[str]) -> None:
		data = FileWorker(paths).get_lines_from_files()
		report = HandlerAuthor(data).create()

		PrinterHandler(report).print()
