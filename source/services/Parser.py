from typing import Union


class ArgvParser:
	"""
	Класс, парсящий аргументы программы
	"""
	def __init__(self):
		self.__expected_long_flags: list[str] = ["--report"]
		self.__expected_short_flags: list[str] = [""]
		self.__argv: list[str] = []

	def set_argv(self,
	             argv: list[str]) -> None:
		"""
		Устанавливает список аргументов, который нужно распарсить
		:param argv:
		:return:
		"""
		if ".py" in argv[0]:
			argv = argv[1:]

		if len(argv) == 0:
			raise TypeError("empty argv list")

		self.__argv = argv

	def get_parsed_argv(self,
	                    argv: list[str] | None = None) -> (list[str], list[str], dict[str: str]):
		"""
		Возвращает распаршенные аргументы
		:return:
		"""
		if argv:
			self.set_argv(argv)
		return self.__get_parsed_argv()

	def __get_parsed_argv(self) -> Union[list[str], list[str], dict[str: str]]:
		"""
		Функция парсит данные, заданные функцией self.set_argv, очишая после парсинга данные.
		:return Union[positional_flags, short_flags, long_flags]:
		"""
		long_flags: dict[str: str] = {}
		short_flags: list[str] = []
		positional_args: list[str] = []

		if not self.__argv:
			raise TypeError("Argv is not defined")

		for idx, arg in enumerate(self.__argv):
			if "--" == arg[:2]:
				if arg not in self.__expected_long_flags:
					raise TypeError(f"{arg} is not expected flag")

				if idx + 1 >= len(self.__argv):
					raise TypeError(f"positional argument expected after {arg}")

				flag_arg = self.__argv[idx+1]
				if "-" == flag_arg[0] or "--" == flag_arg[:2]:
					raise TypeError(f"positional argument expected after {arg}")

				long_flags[arg] = flag_arg

			elif "-" == arg[0]:
				if arg not in self.__expected_short_flags:
					raise TypeError(f"{arg} is not expected flag")

				short_flags.append(arg)
				is_after_flags = True

			elif "." in arg:
				if ".log" not in arg:
					raise TypeError("The extension of the transferred file is not expected.")

				positional_args.append(arg)
		self.__argv = None

		return positional_args, short_flags, long_flags




