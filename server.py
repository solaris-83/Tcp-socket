import socket
from datetime import datetime 
import sys
from stuff import Enumerations
from stuff import dtos
import threading

HOST = "127.0.0.1"      # Symbolic name meaning all available interfaces
PORT = 31001            # Arbitrary non-privileged port
s = None

def handle_client(conn, addr):
    with conn:
            print('Connected by', addr)
            while True:
                try:
                    data = conn.recv(8192)
                    if not data: 
                        continue
                    aux = data.decode("utf-8").split("<")
                    match aux[0]:
                        case OperationTemperatureStartChamberRequest:
                            response = dtos.ResponseDTO(Response=Enumerations.ResponseEnum.Ok, TimeStamp=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
                            print(response.json)
                            js = Enumerations.EnumTopic.OperationTemperatureStartChamberResponse.value + "<" + response.json
                            conn.sendall(js.encode("ascii"))
                except Exception as inst:
                    print(inst)
                    s.close
                    break 

def main():
    global thread
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
            print('listening to incoming connections...')
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)
    try:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        s.close()
        s = None
        print('Stopped socket')
        sys.exit(0)
    finally:
        if thread is not None:
            thread.join()
            print('Thread''s gracefully finished')


if __name__ == '__main__':
    main()

