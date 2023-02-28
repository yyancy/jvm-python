from dataclasses import dataclass


@dataclass
class MethodDescriptor:
  parameter_types: list[str]
  return_type: str
