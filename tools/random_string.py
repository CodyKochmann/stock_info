def random_string(length=32,upper=True,lower=True,digits=True):
  # Generates a random string with selectable characters
  # warning: dont use this for crypto, use a strong cipher.
  # By: Cody Kochmann
  from random import choice
  chars = ""
  if upper:
    chars+="QWERTYUIOPASDFGHJKLZXCVBNM"
  if lower:
    chars+="qwertyuiopasdfghjklzxcvbnm"
  if digits:
    chars+="1234567890"
  return(''.join(choice(chars) for _ in range(length)))

if __name__ == '__main__':
	print(random_string())
