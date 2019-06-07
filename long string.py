#Write your lambda function here
long_string = lambda word: len(word) > 12

print long_string("short")
print long_string("photosynthesis")
