def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
  
    return frequency
def read_words(filename):
    a=open(filename).read().split()
   
    return a
def desc(w):
    d={}
    l=[]
    le=len(w)
    for wo,co in w.items():
      l.append((wo,co))
    
    i=0
    
    while i<le-1:
      j=i+1
      while j<le:
        if l[i][1]<l[j][1]:
          temp=l[i]
          l[i]=l[j]
          l[j]=temp
        j+=1
      i+=1
    return l
        
def main(filename):
    
    frequency = word_frequency(read_words(filename))
    l=desc(frequency)
    for word in l:
        print word[0],word[1]
  

if __name__ == "__main__":
    import sys
    main(sys.argv[1])


