import random

last = 15
rnd_first = random.randint(0, last)
rnd_second = random.randint(0, last)

def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd_first].strip())
  print(quotes[rnd_second].strip())

if __name__== "__main__":
  main()
