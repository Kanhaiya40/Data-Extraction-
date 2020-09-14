purchase_events = open("/home/kanhaiya/Desktop/sample1.txt", "r")

item_id_vs_avg_quantity_per_session = {}
unique_session_id = set({})


def item_id_vs_avg_quantity_per_sessions():
    for each_purchase_event in purchase_events:
        wordlist = each_purchase_event.split(",")
        if wordlist[2] in item_id_vs_avg_quantity_per_session:
            if wordlist[0] in unique_session_id:
                unique_session_id.add(wordlist[0])
                avg = item_id_vs_avg_quantity_per_session.get(wordlist[2]) + float(wordlist[4]) / len(unique_session_id)
                item_id_vs_avg_quantity_per_session.__setitem__(wordlist[2], avg)
            else:
                item_id_vs_avg_quantity_per_session.__setitem__(wordlist[2],
                                                                (item_id_vs_avg_quantity_per_session.get(wordlist[2]) +
                                                                 float(wordlist[4]) / len(unique_session_id)))
        else:
            unique_session_id.clear()
            item_id_vs_avg_quantity_per_session.__setitem__(wordlist[2], float(wordlist[4]))
            unique_session_id.add(wordlist[0])


def print_output():
    for key, value in item_id_vs_avg_quantity_per_session.items():
        print(key, value)


item_id_vs_avg_quantity_per_sessions()
print_output()
