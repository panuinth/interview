  first_line = gets
  t = first_line.to_i

  output = []
  i = 0
  while i < t
    #n,c,m = 0,0,0
    second_line = gets
    n = second_line.split(" ")[0].to_i
    c = second_line.split(" ")[1].to_i
    m = second_line.split(" ")[2].to_i

    discount,piece,temp_piece,free_item = 0,0,0,0

    piece = n / c
    temp_piece = piece

    while (temp_piece >= m)
      discount = temp_piece / m
      free_item = free_item + discount;
      temp_piece = (temp_piece % m) + discount;
    end
    output[i] = piece + free_item

    i = i + 1
  end

  puts output.collect{|x| puts x}

