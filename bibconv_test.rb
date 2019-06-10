# -*- coding: utf-8 -*-
require 'test/unit'

require 'bibconv'

class BibConvTest < Test::Unit::TestCase
  def setup
  end
  
  def teardown
  end

  def test_init
    acmbib = ACMBib.new('1267739')
    puts acmbib.wikititle
    puts acmbib.wikibody
  end
end

