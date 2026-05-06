from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc

class Calculator(service_pb2_grpc.CalculatorServicer):
    def Cube(self, request, context):
        result = request.number ** 3
        return service_pb2.NumberReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()