#Bubble Sort:

#1.Look at the first two items in the list.
#2.If the first item is greater, then swap the items.
#3.Now compare the second and third items in the same way.
#4.Continue doing this until you get to the end of the list - 1.
#5.Repeat the whole process n times (where n is the length of your list).

def bubble_sort(list)
    list.each_index do |i|
      (list.length - i - 1).times do |job|
          if list[job] > list[job + 1]
          list[job], list[job + 1] = list[job + 1], list[job]
          end
      end
    end
end

list = [9, 0, 45, 3, 6, 7, 20, 19, 5]
p list
p bubble_sort(list)
