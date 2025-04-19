from source.models.Report import Report, HandlerReport


class Author:
	"""
	Родительский класс Автор. Поля класса:
	__data: Данные, на основе которых строится отчет.
	__report_fields: Поля отчета, которые следует заполнить
	"""
	__data: list[str]
	__report_fields: list[str]
	def create(self) -> Report:
		"""
		Создает и возвращает объект класса Report
		:return:
		"""
		...

class HandlerAuthor(Author):
	"""
	Автор отчета handlers
	"""
	__LEVELS = [
		'DEBUG',
		'INFO',
		'WARNING',
		'ERROR',
		'CRITICAL'
	]
	__report_fields = [
		'DEBUG',
		'INFO',
		'WARNING',
		'ERROR',
		'CRITICAL'
	]


	def __init__(self,
	             data: list[str]):
		self.__data = data

	def create(self) -> HandlerReport:
		"""
		На основе данных, полученных при инициализации, создает объект класса HandlerReport
		:return:
		"""
		handlers: dict[str: dict[str: int]] = {}


		for log in self.__data:
			parsed_log = log.split()

			if "django.request:" not in parsed_log:
				continue

			parsed_log = parsed_log[2:] # отрезаем дату и время
			level = parsed_log[0]

			if level not in self.__LEVELS:
				continue

			handler = self.__get_handler(
				data=parsed_log
			)

			if handler not in handlers:
				handlers[handler] = {
					field: 0 for field in self.__report_fields
				}

			handlers[handler][level] += 1

		report = self.__create_report(
			data=handlers
		)

		return report


	@staticmethod
	def __get_handler(data: list[str]):
		"""
		Вспомогательный метод для метода create(). В отдельно взятом логе находит handler и возвращает его, иначе возвращает None
		:param data: Распаршенный лог
		:return:
		"""
		for log_part in data:
			if log_part[0] == "/":
				return log_part

	def __create_report(self,
	                    data: dict[str: dict[str: int]]) -> HandlerReport:
		"""
		Создает объект класса репорт на основе словаря data
		:param data: Словарь исходных данных
		:return:
		"""
		output: list[list[int | str]] = []
		handlers = list(data.keys())
		handlers.sort()
		total = 0

		for handler in handlers:
			counts = [data[handler][field] for field in self.__report_fields]
			total += sum(counts)
			cur_output = [handler] + counts

			output.append(cur_output)

		if not output:
			raise TypeError("No value to display")

		return HandlerReport(*list(map(lambda x: list(x), zip(*output))), total)




