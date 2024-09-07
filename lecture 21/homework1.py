import json
with open("movies.json", "r") as json_file:
    data = json.load(json_file)
lst = []
for i in data:
    for j in i['results']:
        list_years = j['release_date'].split("-")
        if int(list_years[0]) > 2000 and "Crime" in j["genres"]:
            index = j["genres"].index("Crime")
            j["genres"][index] = "New_Crime"
            lst.append(j)
            
    
        if int(list_years[0]) < 2000 and "Drama" in j["genres"]:
            index = j["genres"].index("Drama")
            j["genres"][index] = "Old_Drama"
            lst.append(j)
            
            
        if int(list_years[0]) == 2000:
            j["genres"].append("New_Century")
            lst.append(j)
    i['results'] = lst
    lst = []

            
with open("movies.json", "w") as file:
    json.dump(data, file, indent=4)

        

        
    


    
    




