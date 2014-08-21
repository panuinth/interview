   #0:  1: 2: 3:
#0: 1   2  3  4
#1: 5   6  7  8
#2: 9  10 11 12
#3: 13 14 15 16

#1
#2 5
#3 6 9
#4 7 10 13
#8 11 14
#12 15
#16

#[0,0]
#[0,1] [1,0]
#[0,2] [1,1] [2,0]
#[0,3] [1,2] [2,1] [3,0]
#[1,3] [2,2] [3,1]
#[2,3] [3,2]
#[3,3]


input = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

input.each_with_index do | item, i |
  #puts "#{item} row: #{index}"
  item.each_with_index do | element, j|
    #puts "array[#{i}][#{j}] = #{element}"
  end
end

min_row = 0
min_col = 0
max_row = 4
max_col = 4
i = 0
j=0

until i >= max_row
  if i == j
    puts "input[#{i}][#{j}]"
    j = j + 1
  end
  
  if i < (j + 1)
    k = j + 1
    puts "input[#{i}][#{k}]"
  end
  #i += 1
  #j += 1
end


