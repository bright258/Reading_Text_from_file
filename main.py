# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file_read = open(filename, 'r')
    
    return file_read.read()
    


def count_words(filename):
    text = read_file_content(filename)
    # [assignment] Add your code here
    
    dictionary = dict()
    content = text.split()

    for i in content:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    
    print(dictionary)
    return     

count_words('story.txt')