words = ["the", "these", "one", "owner"]
@words_hash = words.each_with_object(Hash.new []) do |word, hash|
  hash[word.chars.sort] += [word]
end

puts @words_hash 
