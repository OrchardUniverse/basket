import argparse
from tabulate import tabulate

from model_client import ModelClient
from maas_config import MaaSConfig, MaaSProvider

client = ModelClient()

# TODO: Hanle fail to parse yaml file
maas_config = MaaSConfig("maas_config.yaml")


def maas_list():
    print("Listing MaaS...")

    maas_providers = maas_config.providers

    # Construct table to print
    data = [["Service", "Available", "Base URL"]]
    align = ("left", "center", "left")
    for provider in maas_providers:
        data.append([provider.name, "*", provider.url])
    print(tabulate(data, headers="firstrow", tablefmt="pretty", colalign=align))

def maas_use(name):
    print(f"Using MaaS: {name}")

def maas_reset():
    pass

def model_list():
    print("Listing models...")

def model_use(name):
    print(f"Using model: {name}")

def list_config():
    print("Listing config...")
    
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
    maas_reset_parser = maas_subparsers.add_parser("reset", help="Reset auths of a specific MaaS")
    maas_reset_parser.add_argument("name", type=str, help="Name of the MaaS to reset")

    # Model command
    model_parser = subparsers.add_parser("model", help="Model related commands")
    model_subparsers = model_parser.add_subparsers(dest="model_command")
    model_subparsers.add_parser("list", help="List models")
    model_use_parser = model_subparsers.add_parser("use", help="Use a specific model")
    model_use_parser.add_argument("name", type=str, help="Name of the model to use")

    # Config command
    query_parser = subparsers.add_parser("config", help="List the current config")

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
    elif args.command == "config":
        list_config()
    elif args.command == "query":
        query(args.text)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()