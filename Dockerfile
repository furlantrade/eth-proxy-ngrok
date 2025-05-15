FROM debian:bookworm-slim

RUN apt update && \
    apt install -y curl git unzip build-essential && \
    curl -L https://foundry.paradigm.xyz | bash && \
    ~/.foundry/bin/foundryup && \
    cp ~/.foundry/bin/anvil /usr/local/bin/anvil

WORKDIR /app
COPY . .

EXPOSE 8545

CMD ["anvil", "--host", "0.0.0.0", "--fork-url", "https://ethereum.publicnode.com", "--chain-id", "1"]
