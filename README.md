# Python Credit Card Validator

Uses the Luhn Algorithm to validate a credit card number.

## Methods

### luhn()
Returns true if valid CC number, false if invalid.

### lenChk()
Returns true if CC number between 8 and 19 digits, false if not.

## Usage

Import the class and make use of its methods:

```Python
# myapp.py
import ccvalidator
c1 = ccvalidator.CcVal("49927398716")
print("Passed Luhn Check? ", c1.luhn()) # returns: True
print("Passed Length Check? ", c1.lenChk()) # returns: True
```


## Links
* [Rosettacode - Luhn test of credit card numbers](https://www.rosettacode.org/wiki/Luhn_test_of_credit_card_numbers)