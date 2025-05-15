import sys
from web3 import Web3

TARGET = sys.argv[1]
AMOUNT = Web3.toWei(sys.argv[2], 'ether')

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
w3.provider.make_request("anvil_impersonateAccount", [TARGET])
sender = w3.eth.account.from_key("0x0000000000000000000000000000000000000000000000000000000000000000")  # dummy

tx = {
    "from": TARGET,
    "to": "0x000000000000000000000000000000000000dead",
    "value": AMOUNT,
    "gas": 21000,
    "gasPrice": w3.eth.gas_price,
    "nonce": w3.eth.get_transaction_count(TARGET),
}
tx_hash = w3.eth.send_transaction(tx)
print("Sent TX:", tx_hash.hex())
