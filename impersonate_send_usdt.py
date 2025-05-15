import sys
from web3 import Web3

TARGET = sys.argv[1]
USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
w3.provider.make_request("anvil_impersonateAccount", [TARGET])

erc20 = w3.eth.contract(address=USDT, abi=[
    {
        "name": "transfer",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"}
        ],
        "outputs": [{"name": "", "type": "bool"}]
    }
])

tx = erc20.functions.transfer("0x000000000000000000000000000000000000dead", 1000000).build_transaction({
    "from": TARGET,
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "nonce": w3.eth.get_transaction_count(TARGET),
})
tx_hash = w3.eth.send_transaction(tx)
print("Sent USDT TX:", tx_hash.hex())
