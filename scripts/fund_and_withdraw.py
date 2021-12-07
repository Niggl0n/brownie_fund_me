from os import access
from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    account = get_account()
    fund_me = FundMe[-1]  # get latest deployed version of contract
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrance fee is: {entrance_fee}.")
    funded = fund_me.fund({"from": account, "value":entrance_fee})

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    withdraw = fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()