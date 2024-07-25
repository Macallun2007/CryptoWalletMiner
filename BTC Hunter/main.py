import bitcoin,requests

keep_running = True
address = ""

print("Start Bitcoin Hunting")
print("---------------------")

#Generate a private by bitcoin molecule
def gen_private_key():
    private_key = bitcoin.random_key()
    public_key = bitcoin.privkey_to_pubkey(private_key)
    address = bitcoin.pubkey_to_address(public_key)
    return private_key, address 

#Check the balance from blockchain api
def check_balance():
  private_key, address = gen_private_key()
  try:
    response = requests.get("https://blockchain.info/balance", params={"active": address})
    response.raise_for_status()
    data = response.json()
    final_balance=data[address]["final_balance"]
    print("Private Key:",private_key)
    print("Present Balance:", final_balance)
    print("---------------------")
    if final_balance != 0:
        with open('FoundAddress.txt', 'a') as f:
            f.write("\n",private_key)
            print("Donate to HCMLXOX:bc1qnk0ftxa4ep296phhnxl5lv9c2s5f8xakpcxmth")
  except Exception as e:
    print("Error:Please Check your Network Connection")
    print(e)

#Start Programme
while keep_running:
    check_balance()