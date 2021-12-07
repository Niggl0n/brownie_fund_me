
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,  # deploy_mock price feed if running on local chain
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,  # in order to decide which price feed to take
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # get pricefeed from testnet
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        # get mock pricefeed for local chain
        price_feed_address = MockV3Aggregator[-1].address

    # deploy main contract, given price feed
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},  # we alwas need an account from which we spin up the contract
         # flag if contract should be verified on net: built in brownie utility -> does not have to be specified in the contract
        publish_source=config["networks"][network.show_active()].get("verify"), 
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()