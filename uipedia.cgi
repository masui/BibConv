#!/home/masui/.rbenv/shims/ruby

require './bibconv'
require 'cgi'

cgi = CGI.new('html3')
url = cgi.params['url'].to_s

if url =~ /dl\.acm/ then
  bib = ACMBib.new(url)
elsif url =~ /ci\.nii\.ac\.jp/ then
  bib = NIIBib.new(url)
else
  exit
end

title = bib.wikititle
body = bib.wikibody


cgi.out {
  cgi.html {
    cgi.head {
      cgi.meta(
        'http-equiv' => "refresh",
        'content' => "1;url=https://scrapbox.io/UIPedia/#{CGI.unescape_html(title)}?body=#{CGI.escape(CGI.unescape_html(body))}"
      )
    }
  }
}

