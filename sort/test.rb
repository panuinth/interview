def quick_sort(list, from=0, to=nil)
  to = list.length - 1 if to.nil?
  return if from >= to

  min = from
  max = to
  free = min
  pivot = list[min]

  while min < max
    if free == min
      if list[max] <= pivot
        list[free] = list[max]
        min += 1
        free = max
      else
        max -= 1

      end
    elsif free == max
      if list[min] > pivot
        list[free] = list[min]
        max -= 1
        free = min
      else
        min += 1
      end
    end
  end
  list[free] = pivot

  quick_sort list,  from , free - 1
  quick_sort list,  free + 1, to
end
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15].shuffle
# Quicksort operates inplace (i.e. in "a" itself)
# There's no need to reassign
puts a.inspect
quick_sort a
puts "quicksort"
puts a.inspect
