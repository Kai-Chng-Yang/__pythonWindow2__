from tools import Taiwan_AQI

def get_best(dataList) -> list:
    sorted_data = sorted(dataList, key=lambda a:a.aqi, reverse=True)
    def out_aqi_999(site):
        return site.aqi != 999
    filter_data = filter(out_aqi_999, sorted_data)
    filter_data = list(filter_data)
    return filter_data[-3:]

def get_bad(dataList) -> list:
    sorted_data = sorted(dataList, key=lambda a:a.aqi, reverse=True)
    def out_aqi_999(site):
        return site.aqi != 999
    filter_data = filter(out_aqi_999, sorted_data)
    filter_data = list(filter_data)
    return filter_data[:3]

def print_site_level(dataList) -> None:
    def out_aqi_999(site):
        return site.aqi != 999
    filter_data = filter(out_aqi_999, dataList)
    for site in filter_data:
        if site.aqi <= 50:
            print(f"{site.site_name}-良好 綠")
        elif site.aqi <= 100:
            print(f"{site.site_name}-普通、黃")
        elif site.aqi <= 150:
            print(f"{site.site_name}-對敏感族群不良 橘")
        elif site.aqi <= 200:
            print(f"{site.site_name}-對所有族群不良 紅")
        elif site.aqi <= 300:
            print(f"{site.site_name}-非常不良、紫")
        else:
            print(f"{site.site_name}-有害、褐紅色")



def main():
    try:
        aqi_list = Taiwan_AQI.download_aqi()
    except Exception as err:
        print(str(err))
        return
    
    good3_list = get_best(aqi_list)
    print("目前空氣aqi品質最好的3個")
    good3_list.reverse()
    for site in good3_list:
        print(site)
    
    print('\n')
    bad3_list = get_bad(aqi_list)
    print("目前空氣aqi品質最差的3個")
    for site in bad3_list:
        print(site)

    print('\n')
    print_site_level(aqi_list)



if __name__ == "__main__":
    main()


