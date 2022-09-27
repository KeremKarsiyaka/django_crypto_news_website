from django.shortcuts import render

def home (request):
	import requests
	import json

	# grab crypto price data
	price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USR&api_key={8cb7ec50e0148557420b67436904961aa531c32d7cef9402f0c9d13fa131146c}')
	price = json.loads(price_request.content)

	# grab crypto news
	api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={8cb7ec50e0148557420b67436904961aa531c32d7cef9402f0c9d13fa131146c}')
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api':api, 'price': price})


def prices(request):
	if request.method == "POST":
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote + '&tsyms=USR&api_key={8cb7ec50e0148557420b67436904961aa531c32d7cef9402f0c9d13fa131146c}')
		crypto = json.loads(crypto_request.content)
		
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
	
	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'notfound': notfound})
	