import wikipedia
search= input("Enter want you want to search: ")
wikipedia.set_lang("hi")
print(wikipedia.summary(search))
close = input("enter to close")
