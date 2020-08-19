word_list = ['xyz','Yxz','zyX'] #INPUT ARRAY

  text = '' #INPUT TEXT
  text = text.replace(',',' ') #these statements remove irrelevant punctuation
  text = text.replace('.','')
  text = text.lower() #this makes all the words lowercase, so that capitalization wont affecting
  for repeatedword in word_list:
          counter = 0 #counter starts at 0
          for word in text.split():
              if repeatedword.lower() == word:

                  counter = counter + 1 #add 1 every time there is a match in the list
          print(repeatedword,':', counter) #prints the word from 'word_list' and its frequency
 
