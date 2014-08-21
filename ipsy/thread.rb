#a = [1,2,-3,4,5,-9]
a = [7,6,-3,-4,0,-5,-2,2]

7 -3 -4
7 -5 -2
6 -4 -2
0 -2 2


def sum_result(a)
  result = {}
  b = a
  a.each_with_index do |val_a, index_a|
    val_a.each_with_index do |val_b, index_b|
      val_b.each_with_index do |val_c, index_c|
        puts "#{val_a} #{val_b} #{val_c}"if (val_a + val_b + val_c).eql?(0)
      end
    end
  end

end

#tim@ipsy.com
#glenn@ipsy.com
