# Define an initial blockcain list
blockchain = [[1]]

# Create a function that returns the last list in the chain
def last_chain_value():
    return blockchain[-1]

# Create a function that inserts transactions into the list
def add_value(transaction_amount, last_transaction= [90]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)

#Ask user for transaction input 
tx_amount = float(input('Please enter your transaction amount: '))
#Test transaction function with default data
add_value(tx_amount)
#Test transaction function by inserting next data
add_value(last_transaction=last_chain_value(), transaction_amount=0.998)
#Test transaction function by inserting next data
add_value(45.90, last_chain_value())