#Ashkan Moghaddassi
#7.12.2021

import tkinter as tk
import algosdk

def createwallet():
    textbox1.delete(0, tk.END)
    textbox1.insert(0, "Account Address: ")
    textbox2.delete(0, tk.END)
    textbox2.insert(0, "Private Key Mnemonic: ")
    # Generate a private key and associated account address
    private_key, account_address = algosdk.account.generate_account()

    # Create a mnemonic phrase for the private key
    mnemonic = algosdk.mnemonic.from_private_key(private_key)

    textbox1.insert(17,account_address)
    textbox2.insert(22, mnemonic)


# Root window info
root = tk.Tk()
root.wm_title("Algorand Wallet Client")

button1 = tk.Button(text='Create Wallet',command= createwallet, fg='black', font = ("Georgia", 12))
button1.pack()

# For new wallet output
textbox1 = tk.Entry(root, width=120)
textbox1.insert(0, "Account Address: ")
textbox1.pack(fill=tk.BOTH)

textbox2 = tk.Entry(root, width=120)
textbox2.insert(0, "Private Key Mnemonic: ")
textbox2.pack(fill=tk.BOTH)
# Starts tkinter
root.mainloop()
