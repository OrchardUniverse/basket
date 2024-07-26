import os
import argparse
import getpass
from tabulate import tabulate

from model_client import ModelClient
from maas_config import MaaSConfig, MaaSProvider
from auths_config import AuthsConfig

import coloredlogs, logging
coloredlogs.install()

# TODO: Hanle fail to parse yaml file
maas_config = MaaSConfig("maas_config.yaml")
auths_config = AuthsConfig("auths_config.yaml")

client = ModelClient(auths_config.get_current_maas(), auths_config.get_current_model())

def maas_list():
    maas_providers = maas_config.providers

    # Construct table to print
    data = [["Service", "API KEY Configured", "Base URL"]]
    align = ("left", "center", "left")
    for provider in maas_providers:
        # TODO: check auths config to get configured MaaS
        data.append([provider.name, "*", provider.url])
    print(tabulate(data, headers="firstrow", tablefmt="pretty", colalign=align))

"""
Use the MaaS as current MaaS. Request for API KEY and update the local configuration file.
"""
def maas_use(name):
    maas_provider = maas_config.get_provider(name)
    if maas_provider == None:
        logging.error("Please use a valid MaaS name in {}. You can add new MaaS in 'maas_config.yaml'.".format(maas_config.list_maas_names()))
        return
    else:
        # Try to set API KEY
        if set_maas_apikey(maas_provider.name):
            # Update local config file
            auths_config.update_current_maas(maas_provider.name)
            client.reload(auths_config)
            logging.info("Success to use MaaS: {}".format(maas_provider.name))

"""
Read environemnt variable or request user to input API KEY for MaaS.
"""
def set_maas_apikey(maas_name: str) -> bool:
    if auths_config.get_auth(maas_name):
        logging.info("API KEY has been initiliazed")
        return True
    else:
        logging.warning("API KEY for {} is not initialized".format(maas_name))

        apikey_env = "{}_API_KEY".format(maas_name.upper())
        logging.info("Try to read {} from environment variable".format(apikey_env))
        apikey = os.getenv(apikey_env, "")
        if apikey == "":
            logging.warning("Fail to load API KEY from environment variable, you can export {}='ak-xxx'".format(apikey_env))

            apikey = getpass.getpass(prompt="Please input the API KEY for {}: ".format(maas_name))
            logging.info("Success to get API KEY from user input")
        else:
            logging.info("Success to get API KEY from environment variable: {}".format(apikey_env))
        
        auths_config.add_auth(maas_name, apikey)
        return True
        
"""
Reset the API KEY for the MaaS.
"""
def maas_reset(name: str) -> None:
    maas_provider = maas_config.get_provider(name)
    if maas_provider == None:
        logging.error("Please use a valid MaaS name in {}. You can add new MaaS in 'maas_config.yaml'.".format(maas_config.list_maas_names()))
        return

    if auths_config.get_auth(name):
        logging.info("API KEY has been initiliazed, remove it")

        if auths_config.remove_auth(name):
            logging.info("Success to remove API KEY for {}".format(name))
        else:
            logging.info("Fail to reset API KEY for {}".format(name))
    else:
        logging.warning("The API KEY for {} is not initialized, ignore it".format(name))

"""
List the available models for MaaS.
"""
def model_list():
    logging.info("Listing models...")
    

def model_use(name):
    # Update local config file
    auths_config.update_current_model(name)
    client.reload(auths_config)
    logging.info("Success to use Model: {}".format(name))

def list_current_config():
    print_maas_info = client.get_maas()
    if print_maas_info == "":
        print_maas_info = "NOT SET (Please run: basket maas use $name)"
    logging.info("Current maas: {}".format(print_maas_info))

    print_model_info = client.get_model()
    if print_model_info == "":
        print_model_info = "NOT SET (Please run: basket model use $name)"
    logging.info("Current model: {}".format(print_model_info))

def query(text):
    logging.info(f"Querying with: {text}")

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
        elif args.maas_command == "reset":
            maas_reset(args.name)
    elif args.command == "model":
        if args.model_command == "list":
            model_list()
        elif args.model_command == "use":
            model_use(args.name)
    elif args.command == "config":
        list_current_config()
    elif args.command == "query":
        query(args.text)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()