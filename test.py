#Here we import the library to make web requests
import urllib2

#Here we make a request to the main web application URL
content = urllib2.urlopen("http://www.projectx.ideape.com/").read()

print "Hi there! Lets check if we can make a connection:"
#And here we print the response we received
#EXPECTED RESPONSE: "Hello world! Welcome to Project X's web server!"
print content