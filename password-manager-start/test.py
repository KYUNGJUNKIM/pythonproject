import json

with open("data.json", "r") as data:
    data_file = json.load(data)
    print(data_file["Naver"]["email"])
    # for i in range(len(data_file)):
    #     for key, value in data_file[i]:
    #         print(key)
    #         print(value)
