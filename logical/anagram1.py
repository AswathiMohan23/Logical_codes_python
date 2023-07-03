
# Given a list of words, efficiently group all anagrams. The two strings, X and Y, are anagrams
# if by rearranging X's letters, we can get Y using all the original letters of X exactly once.
#
# Input : ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED',
# 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
#
# Output:
# {
#     ('CARS', 'ARCS', 'SCAR'),
#     ('REPAID', 'PAIRED'),
#     ('SIGNED', 'DESIGN'),
#     ('LANE', 'LEAN'),
#     ('GRAB', 'BRAG'),
#     ('NOSE', 'ONES'),
#     ('DUES', 'USED', 'SUED')
# }
# Input : ['CARS', 'LANE', 'ONES']
# Output: {}
# The solution should return a set containing all the anagrams grouped together, irrespective of the order.


def anagrams( input_list ):
   dictionary = {}
   for i in input_list:
       sortedWord = ''.join(sorted(i))
       # If word is not in dictionary
       if sortedWord not in dictionary:
           dictionary[sortedWord] = [i]
       # If previously it is present that means its anagram
       else:
           dictionary[sortedWord] += [i]
   return [dictionary[i] for i in dictionary]

if __name__ == '__main__':
   input_list =['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED',
                        'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
   print(anagrams(input_list))



