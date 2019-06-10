#! /usr/bin/ruby

require 'bibconv'
require 'cgi'

cgi = CGI.new('html3')
naidstring = cgi.params['naidstring'].to_s

niibib = NIIBib.new(naidstring)

cgi.out {
  cgi.html {
    cgi.head {
      cgi.title { niibib.wikititle }
    } +
    cgi.body {
      cgi.b { niibib.wikititle } + cgi.p +
      cgi.pre {
        niibib.wikibody
      }
    }
  }
}

