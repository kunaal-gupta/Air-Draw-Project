try:
    from googlesearch import search
except ImportError:
    print('We cannot find the requested module')


query = "Geeksforgeeks"

for data in search(query, tld='ca', lang='en', tbs='0', safe='off', num=10, start=0, stop=None, pause=2.0, country='Canada', extra_params=None, user_agent=None, verify_ssl=True):
	print(data)

