def get(url):
  import requests
  return(requests.get(url,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
  }).text)

if __name__ == '__main__':
	print(get(input('Enter the link to get: ')))
