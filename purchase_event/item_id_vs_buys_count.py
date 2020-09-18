item_id_vs_buys_count = {}

purchase_events = open("/home/kanhaiya/Desktop/sample1.txt", "r")


def item_id_vs_purchase_count():
    for each_purchase_event in purchase_events:
        wordlist = each_purchase_event.split(",")
        if item_id_vs_buys_count.get(wordlist[2]) is not None:
            item_id_vs_buys_count.__setitem__(wordlist[2], item_id_vs_buys_count.get(wordlist[2]) + 1)
        else:
            item_id_vs_buys_count.setdefault(wordlist[2], 1)


def print_output():
    for key, value in item_id_vs_buys_count.items():
        print(key, value)


item_id_vs_purchase_count()
print_output()
purchase_events.close()
