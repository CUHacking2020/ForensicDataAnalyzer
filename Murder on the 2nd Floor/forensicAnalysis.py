
def analyzeFile(filename):
    raw_data = []
    
    file = open(filename,"r")
    count = 0
    
    for line in file:
        count += 1
                 
        if count == 1:
            line_data = []
            
        elif count == 2:
            timestamp = ""
            for char in line:
                if char.isdigit():
                    timestamp = timestamp + char
            line_data.append(timestamp)

        elif count == 3:
            quote_count = 0
            device = ""
            
            for char in line:
                if char == '"':
                    quote_count += 1

                if quote_count == 3:
                    device = device + char
                    
            line_data.append(device[1:])

        elif count == 4:
            quote_count = 0
            device_id = ""
            
            for char in line:
                if char == '"':
                    quote_count += 1

                if quote_count == 3:
                    device_id = device_id + char
                    
            line_data.append(device_id[1:])

        elif count == 5:
            quote_count = 0
            event = ""
            
            for char in line:
                if char == '"':
                    quote_count += 1

                if quote_count == 3:
                    event = event + char
                    
            line_data.append(event[1:])
                    
        else:
            quote_count = 0
            name = ""
            
            for char in line:
                if char == '"':
                    quote_count += 1

                if quote_count == 3:
                    name = name + char
                    
            line_data.append(name[1:])
            
            count = 0
            raw_data.append(line_data)

    return raw_data

def suspect_profiles(filename, suspect):
    data = analyzeFile(filename)
    suspect_info = []
    for event in data:
        if event[4] == suspect:
            suspect_info.append(event)

    return suspect_info

#print(suspect_profiles("Murder-on-the-2nd-Floor-Raw-Data.json","Veronica"))
        

'''def murder_victim(data):
    potential_victims = []
    for event in data:
        if event[2] == "210" and event[1] == "door sensor":
            if event[4] in potential_victims:
                potential_victims.remove(event[4])
                potential_victims.append(event[4])
            else:
                potential_victims.append(event[4])
                
    return potential_victims'''
