# prettyfies json objects

def prettyfy(json_input, indnt=4):
  import json
  return(json.dumps(
    json_input,
    sort_keys=True,
    indent=indnt, 
    separators=(',', ': ')
  ))

if __name__ == '__main__':
	print(prettyfy({
		'test':'success'
	}))
