#Selection Sort:

#1.Take an item in the list and walk up the array checking each element.
#2.If the item is larger, leave it. If it is smaller, walk back down shifting all larger elements up until it becomes the larger element.
#3.You are basically iterating through the list and inserting each item into its correct place.

def insertion_sort(list)
  (1..list.length - 1).each do |i|
    value = list[i]
    j = i - 1
    while j >= 0 && list[j] > value do
      list[j + 1] = list[j]
      j -= 1
    end
    list[j + 1] = value
  end
  list
end

list = [9, 0, 45, 3, 6, 7, 20, 19, 5]
p list
p insertion_sort(list)
