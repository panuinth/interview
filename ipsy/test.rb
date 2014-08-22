a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

#   0   1  2  3
#0 [1 , 2, 3, 4]
#1 [5 , 6, 7, 8]
#2 [9 ,10,11,12]
#3 [13,14,15,16]
#

#1
#2   5
#3   6   9
#4   7  10  13
#8  11  14
#12 15
#16
#

#(0,0)
#(0,1) (1,0)
#(0,2) (1,1) (2,0)
#(0,3) (1,2) (2,1) (3,0)
#(1,3) (2,2) (3,1)
#(2,3) (3,2)
#(3,3)


row = a.count
max = row - 1
col = a.first.count

result = []

i = 0
j = 0

while true

  sub_i = i
  sub_j = j

  while sub_i < row and sub_j >= 0
    puts "(#{sub_i},#{sub_j})"
    result << a[sub_i][sub_j]
    sub_i = sub_i + 1
    sub_j = sub_j - 1
  end

  if j < col - 1
    j = j + 1
  elsif i < row - 1
    i = i + 1
  else
    break
  end

end

p result
