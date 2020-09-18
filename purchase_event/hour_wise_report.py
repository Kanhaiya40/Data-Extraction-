import datetime

hour_count = {}

hour_wise_session_id = {}

hour_wise_item_id = {}

purchase_events = open("/home/kanhaiya/Desktop/sample1.txt", "r")

hour_wise_report_data = set([])


def hour_wise_report():
    for each_purchase_event in purchase_events:
        wordlist = each_purchase_event.split(",")
        date_time = (datetime.datetime.strptime(wordlist[1], "%Y-%m-%dT%H:%M:%S.%fZ"))
        hour_with_week_day = tuple(
            [date_time.strftime("%A") + "_" + str(date_time.hour) + "_" + str(date_time.hour + 1)])
        if hour_with_week_day not in hour_count:
            unique_session_id = set([])
            unique_session_id.add(wordlist[0])
            unique_item_id = set([])
            unique_item_id.add(wordlist[2])
            hour_wise_item_id.__setitem__(hour_with_week_day, unique_item_id)
            hour_wise_session_id.__setitem__(hour_with_week_day, unique_session_id)
            hour_count.setdefault(hour_with_week_day, 1)
            hour_wise_data = tuple([hour_with_week_day,
                                    (len(hour_wise_session_id.get(hour_with_week_day)) / hour_count.get(
                                        hour_with_week_day)),
                                    (len(hour_wise_item_id.get(hour_with_week_day)) / hour_count.get(
                                        hour_with_week_day))])
            hour_wise_report_data.add(hour_wise_data)

        else:
            updated_unique_session_id = hour_wise_session_id[hour_with_week_day]
            updated_unique_session_id.add(wordlist[0])
            hour_wise_session_id[hour_with_week_day] = updated_unique_session_id
            updated_unique_item_id = hour_wise_item_id[hour_with_week_day]
            updated_unique_item_id.add(wordlist[2])
            hour_wise_item_id[hour_with_week_day] = updated_unique_item_id
            hour_count.__setitem__(hour_with_week_day, hour_count.get(hour_with_week_day) + 1)
            hour_wise_data = tuple([hour_with_week_day,
                                    (len(hour_wise_session_id.get(hour_with_week_day)) / hour_count.get(
                                        hour_with_week_day)),
                                    (len(hour_wise_item_id.get(hour_with_week_day)) / hour_count.get(
                                        hour_with_week_day))])
            hour_wise_report_data.add(hour_wise_data)


def print_output():
    print(hour_wise_report_data)


hour_wise_report()
print_output()
