def quick_sort(array, from=0, to= array.length - 1)

  return if to < from

  min = from
  max = to
  free = min
  pivot = array[min]

  while min < max
    if free == min
      if array[max] <= pivot
        array[free] = array[max]
        min += 1
        free = max
      else
        max -= 1
      end
    elsif free == max
      if array[min] >= pivot
        array[free] = array[min]
        max -= 1
        free = min
      else
        min += 1
      end

    end
  end

  quick_sort array, from, free - 1
  quick_sort array, free + 1, to
end

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15].shuffle
# Quicksort operates inplace (i.e. in "a" itself)
# There's no need to reassign
p a
quick_sort a
puts "quicksort"
puts a.inspect

