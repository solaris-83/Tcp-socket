from json import dumps
from dataclasses import dataclass

@dataclass
class ResponseDTO:
    def __init__(self, Response, TimeStamp):        
        self.Response = Response
        self.TimeStamp = TimeStamp
            
    @property
    def json(self):
        return dumps(self, default=lambda o: o.__dict__)  