import os

from dotenv import load_dotenv

from iota_sdk import SendNftParams, Wallet

load_dotenv()

# In this example we will send an nft

wallet = Wallet(os.environ['WALLET_DB_PATH'])

if 'STRONGHOLD_PASSWORD' not in os.environ:
    raise Exception(".env STRONGHOLD_PASSWORD is undefined, see .env.example")

wallet.set_stronghold_password(os.environ["STRONGHOLD_PASSWORD"])

account = wallet.get_account('Tomy')

# Sync account with the node
balance = account.sync()

outputs = [SendNftParams(
    address="rms1qpszqzadsym6wpppd6z037dvlejmjuke7s24hm95s9fg9vpua7vluaw60xu",
    nftId=balance.nfts[0],
)]

transaction = account.send_nft(outputs)
print(f'Block sent: {os.environ["EXPLORER_URL"]}/block/{transaction.blockId}')