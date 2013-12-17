from bottle import TornadoServer, run
from renting_routing import app as application
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description="Hardware Rental server")
    parser.add_argument("-p", "--port", action="store", type=int, dest="port")
    args = parser.parse_args()
    if args.port:
        run(application, server='tornado', port=args.port)
    else:
        run(application, server='tornado', port=8101)