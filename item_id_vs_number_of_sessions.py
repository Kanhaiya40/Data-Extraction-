itemid_vs_numberOfSession = {}

purchase_events = open("/home/kanhaiya/Desktop/sample1.txt", "r")


def item_id_vs_number_of_session():
    for each_purchase_event in purchase_events:
        wordlist = each_purchase_event.split(",")
        if itemid_vs_numberOfSession.get(wordlist[2]) == None:
            unique_sessionid = set([])
            unique_sessionid.add(wordlist[0])
            itemid_vs_numberOfSession.setdefault(wordlist[2], unique_sessionid)
        else:
            updated_unique_sessionid = itemid_vs_numberOfSession[wordlist[2]]
            updated_unique_sessionid.add(wordlist[0])
            itemid_vs_numberOfSession[wordlist[2]] = updated_unique_sessionid


def print_output():
    for key, value in itemid_vs_numberOfSession.items():
        print(key, len(value))


item_id_vs_number_of_session()
print_output()
