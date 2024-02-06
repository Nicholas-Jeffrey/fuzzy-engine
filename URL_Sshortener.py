import pyshorteners

#URL shortner with tinyurl

 

long_url = input("Please enter URL to shorten: ")

type_tiny = pyshorteners.shortener()

 

short_url = type_tiny.tinyurl.short(long_url)

print("The shortened URL is: " + short_url)

 

 

import pyshorteners

long_url = input("Enter the URL to shorten: ")

 

#Bitly shortener service

type_bitly = pyshorteners.Shortener(api_key='01b6c587cskek4kdfijsjce4cf27ce2')

short_url = type_bitly.bitly.short('https://www.google.com')

 

print("The Shortened URL is: " + short_url)

#url expanding getting the total number of clicks

expand_url = type_bitly.bitly.expand('https://bit.ly/TEST')

print (expand_url) # gives the url in expand or original form

 

count = type_bitly.bitly.total_clicks('https://bit.ly/TEST') #gives total no. of clicks.