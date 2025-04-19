import os.path
from os.path import abspath

class FileWorker:
	"""
	Открытие файлов и выгрузка из них информации
	"""
	def __init__(self,
	             paths: list[str]):
		self.__paths = paths

	def get_lines_from_files(self
	                         ) -> list[str]:
		"""
		Метод, парсящий все переданные файлы.
		:return: Все строки файлов, переданных при инициализации
		"""

		output = []
		for path in self.__paths:
			lines = self.__get_lines_from_file(path)
			output += lines

		return output

	@staticmethod
	def __get_lines_from_file(path: str
	                          ) -> list[str]:
		"""
		Парсит файл на список строк
		:param path: Путь до файла
		:return: Все строки файла
		"""
		if not (os.path.exists(path)):
			raise TypeError(f"file {path} doesn't exists")

		absolute_path = abspath(path)
		with open(absolute_path, 'r') as f:
			return [line.strip() for line in f.readlines()]


