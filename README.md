# Anvil Impersonation RPC

Este projeto inicia um nó Anvil no Railway com fork da mainnet Ethereum.

## Uso

Inicie com:
```
anvil --host 0.0.0.0 --fork-url https://ethereum.publicnode.com --chain-id 1
```

Depois, acesse via `https://seu-projeto.up.railway.app`.

## Scripts

```bash
python impersonate_send.py <address> <eth_amount>
python impersonate_send_usdt.py <address>
```
