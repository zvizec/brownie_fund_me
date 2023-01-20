from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    print(f"FundMe: {fund_me}")
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    latest_price = fund_me.getLatestPrice()
    entrance_fee_eth = entrance_fee/10**18
    latest_price_usd = latest_price/10**18
    
    print(f"Latest price {latest_price/10**18} USD")
    print(f"Entrance fee {entrance_fee} wei")
    print(f"             {entrance_fee/10**18} ETH")
    print(f"             {entrance_fee_eth*latest_price_usd} USD")
    
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    
    
def main():
    fund()
    withdraw()