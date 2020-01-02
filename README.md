# Python Credit Card Validator

Uses the (Luhn Algorithm)[https://www.rosettacode.org/wiki/Luhn_test_of_credit_card_numbers] to validate a credit card number

## Methods

luhn()
Returns true if valid CC number, false if invalid.

lenChk()
Returns true if CC number between 8 and 19 digits, false if not.

## Usage

```Python
import ccvalidator

c1 = CcValidator("49927398717")
print(c1.luhn())
print(c1.lenChk())
```