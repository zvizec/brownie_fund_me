from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    
    tx = fund_me.withdraw({"from":account})
    tx.wait(1)
    assert fund_me.balance() == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")
    fund_me = deploy_fund_me()
    account=get_account()
    print("good ", account)
    bad_actor = accounts.add() # blank random account
    print(accounts)
    print("BAD ", bad_actor)
    with pytest.raises(exceptions.Valu):
        entrance_fee = fund_me.getEntranceFee() + 100
        print(entrance_fee)
        tx = fund_me.fund({"from": account, "value": entrance_fee})
        receipt=tx.wait(1)
        print("ADDR ",tx)
        fund_me.withdraw({"from": bad_actor})