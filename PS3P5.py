FixedCost = float(input("We need to determine our break even point.  How much are our fixed production costs at the company? $"))
PPU = float(input("\nHow much are we charging for each unit? $"))
CPU = float(input("\nHow much does it cost us to produce each unit? $"))

BEP = float((FixedCost)/(PPU-CPU))

print(f"\nIt appears that our break even point is ${BEP:.2f}.")