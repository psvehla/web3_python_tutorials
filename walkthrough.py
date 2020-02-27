# Put your imports here
import os
from web3 import Web3, HTTPProvider
from interface import ContractInterface

# Initialize your web3 object
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# Create a path object to your Solidity source files
contract_dir = os.path.abspath('./contracts/')

# Initialize your interface
greeter_interface = ContractInterface(w3, 'Greeter', contract_dir)
greeter_interface.compile_source_files()
greeter_interface.deploy_contract()
instance = greeter_interface.get_instance()
instance.functions.greet().call()
