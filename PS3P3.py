PriceMeal = float(input("How much did you pay for your meal? "))

print("We have three tip options and they are as follows\n")

print("With a 15% tip:")
print(f"Total: $ {PriceMeal:.2f}")
print(f"Tip: ${PriceMeal * 0.15:.2f}")
print(f"Total with Tip: ${(PriceMeal*0.15)+PriceMeal:.2f}\n")

print("With a 18% tip:")
print(f"Total: $ {PriceMeal:.2f}")
print(f"Tip: ${PriceMeal * 0.18:.2f}")
print(f"Total with Tip: ${(PriceMeal*0.18)+PriceMeal:.2f}\n")

print("With a 20% tip:")
print(f"Total: ${PriceMeal:.2f}")
print(f"Tip: ${PriceMeal*0.2:.2f}")
print(f"Total with Tip: ${(PriceMeal*0.2)+PriceMeal:.2f}")