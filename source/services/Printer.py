from source.models.Report import Report, HandlerReport


class Printer:
	"""
	Родительский класс, предназначенный для вывода отчетов в консоль
	Поля: __report - отчет, который нужно вывести
	Методы: print() - вывод отчета
	"""
	__report: Report
	def print(self):
		...


class PrinterHandler(Printer):
	"""
	Класс, предназначенный для вывода отчета Handler в консоль
	"""
	__report: HandlerReport
	def __init__(self, report: HandlerReport):
		self.__report = report

	def set_report(self, report: HandlerReport):
		self.__report = report

	def __prepare(self):
		"""
		"Подготовка к выводу", создание необходимых условий и задание нужных переменных
		:return:
		"""
		values = {
			"handlers": list(self.__report.handlers),
			"debug": list(self.__report.debug),
			"info": list(self.__report.info),
			"warning": list(self.__report.warning),
			"error": list(self.__report.error),
			"critical": list(self.__report.critical),
		}
		total = self.__report.total
		#Хранит в себе количество символов + 5, нужных для записи конкретного столбца
		mx_len_values = [
			max(map(lambda x: len(str(x)) + 5, values[key] + [key])) for key in list(values.keys())
		]

		output_length = len(values["handlers"])

		values_to_output = list(zip(*[value for value in list(values.values())]))
		return values_to_output, mx_len_values, output_length, total

	@staticmethod
	def __create_output_string(values: list[str],
	                           mx_len_values: list[int]) -> str:
		"""
		На основе переданных значений отдает строку, которую следует вывести
		:param values: Значение строки
		:param mx_len_values: Длина вывода конкретных значений
		:return:
		"""
		output = ''

		for idx in range(len(values)):
			value = values[idx]
			length = mx_len_values[idx]

			result = str(value) + " " * (length - len(str(value)))

			output += result

		return output

	def __create_header(self,
	                    mx_len_values: list[int]) -> str:
		value = [
			"handlers",
			"debug",
			"info",
			"warning",
			"error",
			"critical",
		]
		return self.__create_output_string(
			value,
			mx_len_values
		)


	def print(self):
		"""
		Метод, организующий вывод в консоль отчета.
		:return:
		"""
		values, mx_len_values, output_length, total = self.__prepare()

		print(f"Total requests: {total}")
		print(self.__create_header(mx_len_values))

		for idx in range(output_length):
			value = values[idx]
			print(self.__create_output_string(list(value), mx_len_values))



