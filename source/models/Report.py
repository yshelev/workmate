from dataclasses import dataclass



@dataclass
class Report:
	...

@dataclass
class HandlerReport(Report):
	handlers: list[str]
	debug: list[int]
	info: list[int]
	warning: list[int]
	error: list[int]
	critical: list[int]
	total: int


