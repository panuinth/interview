class Array
  def bin_search(tf,left=0,right=length - 1)
    mid = (left+right)/2
    tf < self[mid] ? right = mid - 1 : left = mid + 1
    tf == self[mid] ? mid : bin_search(tf, left, right)
  end
end

p (0..100).to_a.bin_search(66)

