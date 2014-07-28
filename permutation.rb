#/usr/bin/env ruby

def generate_next_permutation(list)
  # Deal with lists of zero length or empty lists
  if list.length <= 1
    return false
  end

  # Start from the second last element
  i = list.length - 2

  # Go backwards and find the first element which is
  # less than the one immediately after it.
  # This is pointed to by i.
  until list[i] < list[i+1]
    i = i - 1
  end

  # List is in reverse order, finished
  if i < 0
    return false
  end

  # Starting from the last element and going backwards
  # through the list, find the first element which is
  # greater than the element pointed to by i.
  j = list.length - 1
  until list[j] > list[i]
    j = j - 1
  end

  # Swap elements i and j
  #puts "i : #{i} j : #{j}"

  list[i], list[j] = list[j], list[i]
  #puts "SWAP"

  # Reverse the list from i+1 to the end
  i = i + 1
  j = list.length - 1
  until j < i
    list[i], list[j] = list[j], list[i]
    #puts "SWAP INSIDE"
    i = i + 1
    j = j - 1
  end
  return true
end

list = [1,2,3,4,5]
print list.to_s + "\n"
while generate_next_permutation(list) == true
  print list.to_s + "\n"
end
