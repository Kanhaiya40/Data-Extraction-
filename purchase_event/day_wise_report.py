import datetime

purchase_events = open("/home/kanhaiya/Desktop/sample1.txt", "r")

day_count_item_id = {}
day_wise_avg_quantity_report_per_item_id = {}


def day_wise_report():
    for each_purchase_event in purchase_events:
        wordlist = each_purchase_event.split(",")
        day_item_id = tuple(
            [(datetime.datetime.strptime(wordlist[1], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%A")), wordlist[2]])
        if day_item_id in day_count_item_id and day_wise_avg_quantity_report_per_item_id:
            day_count_item_id.__setitem__(day_item_id, day_count_item_id.get(day_item_id) + 1)
            day_wise_avg_quantity_report_per_item_id[day_item_id] = (day_wise_avg_quantity_report_per_item_id.get(
                day_item_id) + float(wordlist[4])) / day_count_item_id.get(day_item_id)
        else:
            day_count_item_id.setdefault(day_item_id, 1)
            day_wise_avg_quantity_report_per_item_id.setdefault(day_item_id,
                                                                float(wordlist[4]) / day_count_item_id.get(day_item_id))


def print_output():
    for key, value in day_wise_avg_quantity_report_per_item_id.items():
        print(key, value)


day_wise_report()
print_output()

purchase_events.close()
