#Merge Sort:

#1.Divide the unordered list in half recursively until we have sublists containing 1 element each.
#2.Repeatedly merge the sublists back together again.

def merge_sort(list)
  return list if list.size < 2
  left = list[0, list.length/2]
  right = list[list.length/2, list.length]

  merge(merge_sort(left), merge_sort(right))
end

def merge(left, right)
  sorted_list = []
  until left.empty? || right.empty?
    sorted_list << (left[0] <= right[0] ? left.shift : right.shift)
  end
  sorted_list.concat(left).concat(right)
  p sorted_list
end

list = [9, 0, 45, 3, 6, 7, 20, 19, 5]
p list
p merge_sort(list)
