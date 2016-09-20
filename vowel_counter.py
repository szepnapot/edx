def countVowels(string, searchFor):
    return sum([1 for c in string if c in searchFor])


print(countVowels('Massachusetts Institute of Technology', 'o'))