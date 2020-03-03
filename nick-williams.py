# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:06:31 2020

@author: peter
"""

import os
from web3 import Web3, HTTPProvider
from interface import ContractInterface

w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))

contractDir = os.path.abspath("./contracts/")

soapBoxInterface = ContractInterface(w3, "SoapBox", contractDir)

soapBoxInterface.compile_source_files()

soapBoxInterface.deploy_contract()

instance = soapBoxInterface.get_instance()
print("before we pay:", instance.functions.isApproved(w3.eth.accounts[0]).call())
instance.functions.pay().transact({'value': w3.toWei(0.03, 'ether')})
print("after we pay:", instance.functions.isApproved(w3.eth.accounts[0]).call())
instance.functions.broadcastOpinion('You can never be overdressed or overeducated.').transact()
print(instance.functions.getCurrentOpinion().call())
