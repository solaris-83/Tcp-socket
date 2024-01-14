from enum import Enum

class EnumTopic(Enum):
    OperationTemperatureStartChamberRequest = "operation/temperature/start/chamber/request"
    OperationTemperatureStartChamberResponse = "operation/temperature/start/chamber/response"
    
class ResponseEnum(int, Enum):
    Nok = 0
    Ok = 1