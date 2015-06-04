bank_csv_python
===============

This program finds unexplained transactions (out-going & incoming) in
a shared back-account. It calculates debits and credits for each
user of the bank account. This allows the user to use these figures
to distribute any surplus money fairly, with evidence.
It has been tested (02/2014) for both Westpac and KiwiBank (NZ only).

In order to use this scipt, you must have [Python 3](https://www.python.org/downloads/release/python-341/ "Python 3 download link") installed and have it added to your $PATH.

`$ python3 shared_bank.py example.csv > output.txt`

___

Im wanting to add graph functionality in the near future, so if you have any experience generating reports with Python, I'd love to hear what you recommend! 
