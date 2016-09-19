import pickle
import zmq

def receiver():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:22334")

    while True:
        try:
            data = pickle.loads(socket.recv())
            print(data)
            socket.send(pickle.dumps(b"ok"))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    receiver()
