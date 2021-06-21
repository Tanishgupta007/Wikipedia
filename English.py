import wikipedia
search= input("Enter want you want to search: ")
wikipedia.set_lang("en")
print(wikipedia.summary(search))
close = input("enter to close")
