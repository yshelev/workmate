from dataclasses import dataclass



@dataclass
class Report:
	"""
	Класс, содержащий в себе информацию по отчету
	"""
	...

@dataclass
class HandlerReport(Report):
	"""
	Класс, содержащий в себе информацию по отчету Handlers
	"""
	handlers: list[str]
	debug: list[int]
	info: list[int]
	warning: list[int]
	error: list[int]
	critical: list[int]
	total: int


