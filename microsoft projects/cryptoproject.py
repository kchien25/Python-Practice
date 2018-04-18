def normalizeText(string):
    string_list = list(string)
    print(string_list)
    for x in string:
        if x.isalpha() == False:
            string_list.remove(x)
    string_list = "".join(string_list).upper()
    print(string_list)

normalizeText("This is some \"really\" great. (Text)!?");