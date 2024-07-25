import argparse
from model_client import ModelClient
from maas_config import MaaSConfig, MaaSProvider


client = ModelClient()
config = MaaSConfig("maas_config.yaml")


def maas_list():
    print("Listing MaaS...")

def maas_use(name):
    print(f"Using MaaS: {name}")

def model_list():
    print("Listing models...")

def model_use(name):
    print(f"Using model: {name}")

def query(text):
    print(f"Querying with: {text}")

def main():
    parser = argparse.ArgumentParser(description="The MaaS management tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # MaaS command
    maas_parser = subparsers.add_parser("maas", help="MaaS related commands")
    maas_subparsers = maas_parser.add_subparsers(dest="maas_command")
    maas_subparsers.add_parser("list", help="List model as a service")
    maas_use_parser = maas_subparsers.add_parser("use", help="Use a specific MaaS")
    maas_use_parser.add_argument("name", type=str, help="Name of the MaaS to use")

    # Model command
    model_parser = subparsers.add_parser("model", help="Model related commands")
    model_subparsers = model_parser.add_subparsers(dest="model_command")
    model_subparsers.add_parser("list", help="List models")
    model_use_parser = model_subparsers.add_parser("use", help="Use a specific model")
    model_use_parser.add_argument("name", type=str, help="Name of the model to use")

    # Query command
    query_parser = subparsers.add_parser("query", help="Perform a query")
    query_parser.add_argument("text", type=str, help="Query text")

    args = parser.parse_args()

    if args.command == "maas":
        if args.maas_command == "list":
            maas_list()
        elif args.maas_command == "use":
            maas_use(args.name)
    elif args.command == "model":
        if args.model_command == "list":
            model_list()
        elif args.model_command == "use":
            model_use(args.name)
    elif args.command == "query":
        query(args.text)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()