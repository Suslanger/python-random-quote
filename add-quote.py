def main():

  f=open("quotes.txt", "a")
  f.write("Now the file has more content!\n")
  f.close()

  f_read=open("quotes.txt")
  print(f_read.read())


if __name__ == "__main__":
  main()
