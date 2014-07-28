#1.Select an element close to the middle (called the pivot element)
#2.Put all elements that are less than or equal to that element to the left.
#3.Put all elements which are greater to its right.
#4.Recursively call this method on the sublists.

def quick_sort(list)
  sl = list.clone
  return sl if sl.size <= 1
  pivot = sl.pop
  left, right = sl.partition { |e| e < pivot }
  quick_sort(left) + [pivot] + quick_sort(right)
end

list = [9, 0, 45, 3, 6, 7, 20, 19, 5]
p list
p quick_sort(list)
