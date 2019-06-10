#! /usr/bin/ruby

require 'bibconv'
require 'cgi'

cgi = CGI.new('html3')
doistring = cgi.params['doistring'].to_s

acmbib = ACMBib.new(doistring)

cgi.out {
  cgi.html {
    cgi.head {
      cgi.meta('http-equiv' => "Content-Type", 'content' => "text/html; charset=utf-8")
    } +
    cgi.body {
      cgi.b { acmbib.wikititle } + cgi.p +
      cgi.pre {
        acmbib.wikibody
      }
    }
  }
}

