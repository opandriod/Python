# Write a program to fill in a letter template given below with name and date.
# letter = '''Dear <|Name|>,
                # you are selected!
                # <|Date|>
                # '''
letter = '''Dear <|Name|>,
  you are selected!
<|Date|>
                '''
print(letter.replace("<|Name|>","Vanlalawmpuia Fanai").replace("<|Date|>","05-FEB-2027"))