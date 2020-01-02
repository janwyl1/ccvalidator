import ccvalidator

c1 = ccvalidator.CcVal("49927398716")
print("Passed Luhn Check? ", c1.luhn())
print("Passed Length Check? ", c1.lenChk())