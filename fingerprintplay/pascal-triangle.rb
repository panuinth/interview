# Enter your code here. Read input from STDIN. Print output to STDOUT
k = gets
k = k.to_i

return if k < 1

output = [[1]]
(k - 1).times do |i|
  output << output[i].inject([1]) do |result, elem|
    output[i].length == result.length ?  result << 1 : result << elem + output[i][result.length]
  end
end

puts output.collect{|x| x.map{|i| i }.join(" ")}
