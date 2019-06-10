#! /usr/bin/ruby
#print "Content-type: text/plain\r\n\r\n"
#print "aaaaa bbbbbb#{ENV['QUERY_STRING']}\r\n"

require 'cgi'

cgi = CGI.new('html3')


# (use acrive record)
s = 100*200

cgi.out {
  cgi.html {
    (0..10).collect {
      cgi.li { "abc" }
    }.join
  }
}

