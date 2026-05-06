import grpc
import service_pb2
import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.CalculatorStub(channel)
        response = stub.Cube(service_pb2.NumberRequest(number=5))
        print(f"Cube of 5 is {response.result}")

if __name__ == "__main__":
    run()