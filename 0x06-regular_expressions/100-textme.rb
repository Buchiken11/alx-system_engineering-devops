#!/usr/bin/env ruby
str1 = ARGV[0].scan(/\[from:([^\]]*)/).join
str2 = ARGV[0].scan(/\[to:([^\]]*)/).join
str3 = ARGV[0].scan(/\[flags:([^\]]*)/).join

puts str1.concat(",").concat(str2).concat(",").concat(str3)
