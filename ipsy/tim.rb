#a = [1,2,-3,4,5,-9]
input = [7,6,-3,-4,0,-5,-2,2]
a = [[input,input,input]]
a = [7,6,-3,-4,0,-5,-2,2]

#7 -3 -4
#7 -5 -2
#6 -4 -2
#0 -2 2
result = []
a = [7,6,-3,-4,0,-5,-2,2]
n = a.count
max = n - 1

for i in 0..(n - 3)
  j = i + 1
  k = i + 2

  x = a[i]
  y = a[j]
  z = a[k]

  while j <= max - 1 and k <= max

    k_index = k
    while k_index <= max

      if a[i] + a[j] + a[k_index] == 0
        puts "a[i]: #{a[i]} a[j]: #{a[j]} a[k]: #{a[k_index]}"
      end
      k_index = k_index + 1
    end

    k = k + 1
    j = j + 1
  end


end

#a.each_with_index do |item_a, index_a|
  #item_a.each_with_index do |item_b, index_b|
    #item_b.each_with_index do |item_c, index_c|
      #if not item_a[index_a][index_b] == item_b[index_b] and item_b[index_b] == item_c
        ##puts "item_a : #{item_a[index_a][index_b]} item_b : #{item_b[index_b]} item_c : #{item_c}"
      #else

        #puts "item_a : #{item_a[index_a][index_b]} item_b : #{item_b[index_b]} item_c : #{item_c}"
      #end
      ##puts "item_a : #{item_a[index_a][index_b]} item_b : #{item_b[index_b]} item_c : #{item_c}" if (item_a[index_a][index_b] + item_b[index_b] + item_c) == 0

      ##puts "item_a : #{item_a[0][0]} item_b : #{item_b[0]} item_c : #{item_c}" if (item_a[0][0] + item_b[0] + item_c) == 0

    #end
  #end
    #puts "-----------------------------"
#end


#p a.inspect

