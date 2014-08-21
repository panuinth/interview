a = [1,3,5,7]
b = [2,9,4,7,1]
c = [3,0,8,1]

#{1: 1, 7: 1, 3:1, 5:1}
#{2:1, 9: 1, 4: 1, 7: 2, 1 : 2, 3:1, 5:1 }
#{3: 2 , 0:1, 8:1, 1:3, 2:1, 9:1, 4:1, 7:2, 5:1 }
#
#Ans {"1"=>3, "3"=>2, "5"=>1, "7"=>2, "2"=>1, "9"=>1, "4"=>1, "0"=>1, "8"=>1}
result = {}

def iterate(list_a, result)

  list_a.each do |item_a|
    if not result["#{item_a}"]
      result["#{item_a}"] = 1
    else
      result["#{item_a}"] = result["#{item_a}"] + 1
    end
  end

  return result
end

p iterate(a,result)
p iterate(b,result)
p iterate(c,result)
