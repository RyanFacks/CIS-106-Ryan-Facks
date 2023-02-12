numstock = int(input("Hello, how many shares of our stock do you hold? "))
initialprice = float(input("How much was each share going for before? "))
newprice = float(input("How muich is each share going for now "))

stockvaluechange = (newprice - initialprice) * numstock

print(f"It appears your stock holdings have changed by an amount of ${stockvaluechange}.")

input("Press enter to exit.")