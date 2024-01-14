from datetime import datetime
from stuff import Enumerations
import socket
import sys
import threading
#from events import Events
from stuff import dtos

class TcpClient():
    client = None
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)    

    def SendMessage(self):
        msg =  str(Enumerations.EnumTopic.OperationTemperatureStartChamberRequest) + '<'
        print(msg)
        client.sendall(msg.encode("ascii")) 

    def run(self):
        try:
            global client
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
        except OSError as msg:
            print(msg)
            client.close()
            client = None
            print('could not open socket')
            return
        if client is not None:
            threading.Timer(1, self.SendMessage).start()
    ''' with s:
            while processor.running:
                try:
                    data = s.recv(8192)
                    if not data:
                        continue
                    aux = data.decode("utf-8").split("<")
                    msg = data.decode("utf-8")
                    match aux[0]:
                        case OperationTemperatureStartChamberResponse:
                            events.ReceivedApplicationMessage(msg)
                except Exception as inst:
                    print(inst)
                    s.close
                    break

        self.processor_thread = processor_thread()
        self.running = True   
        self.processor_thread.start()   '''
  
if __name__ == '__main__':       
    tcpclient = TcpClient('127.0.0.1', 31001)
    tcpclient.run()