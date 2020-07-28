cryptoCurrencyName = input('cryptocurrency name: ')
quantityAvailable = float(input('Quantity Available of ' + str(cryptoCurrencyName) + ' in your account: '))
quotationInUsd = float(input('Quotation of ' + str(cryptoCurrencyName) + ' in $USD: '))
totalValue = quantityAvailable * quotationInUsd
print('Total $USD available in your account: ' + str(totalValue))