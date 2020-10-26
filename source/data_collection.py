import requests
import pprint
import time
import simplejson
start = time.time()

def gen_api_endpoint(end_point):
    prefix = "https://electionsapi.cp.org/api"
    api_group = "federal2019"
    url = r"/".join([prefix,api_group,end_point]) 

    if requests.get(url).status_code == 200:
        return url
    else:
        return 1

 


def filter_parties():
    try:
        party_url = gen_api_endpoint("Parties")
        
        if party_url == 1:
            raise Exception

        data = requests.get(party_url).json()
    
        parties = [party for party in data if party["MajorParty"] == 1]
        
        return parties
    
    except:
        return []
    

    

# returns total number of ridings 
def find_all_ridings():
    endpoint = "Ridings"
    url = gen_api_endpoint(endpoint)
    response = requests.get(url)
    data = response.json()

    return len(data)

def process_data(data):
    temp_dict1 = {
        "RidingNumber":0,
        "RidingName_En":"",
        "RidingName_Fr":"",
        "TotalVotes":0,
        "TurnOut":0,
        "CON":0,
        "LIB":0,
        "NDP":0,
        "GRN":0,
        "BQ":0,
        "PPC":0
    }
    temp_dict2 = {
        "RidingNumber":0,
        "LIB":"",
        "NDP":"",
        "CON":"",
        "GRN":"",
        "BQ":"",
        "PPC":""
    }

    #extract the common info 
    for key in list(temp_dict1.keys())[:4]:
        if key == "RidingNumber":
            temp_dict2[key] = data[0][key]
        temp_dict1[key] = data[0][key]
    
    temp_dict1["TurnOut"] = round(data[0]["TotalVotes"]/data[0]["TotalVoters"],2)
    
    for info in data:
        party_short = info["PartyShortName_En"]
        if party_short in temp_dict1.keys():
            temp_dict1[party_short] = round(info["Votes"]/temp_dict1["TotalVotes"],3)
            temp_dict2[party_short] = info["First"] + " " + info["Last"]
            # if temp_dict2[party_short] == " ":
            #     temp_dict2[party_short] = ''

    return [temp_dict1,temp_dict2]


def get_riding_info(total_ridings):
    data_blob = []
    # trim the last 1 , since its a perimeter
    url_temp = gen_api_endpoint("Candidates_For_Riding?ridingnumber=1")[:-1]
    success_count = 0
    fail_count = 0

  
    for i in range(1,total_ridings+1):
        url = url_temp + str(i)
        try :
            # print(url)
            
            data = requests.get(url).json()
            processed_data = process_data(data)
            success_count += 1
        except simplejson.errors.JSONDecodeError:
            # sometimes the api fails, wait for 2 sec and try again with the failed url 
            fail_count += 1
            time.sleep(2)
            # response = requests.get(url)
            while True:
                response = requests.get(url)
                if response.status_code == 200:
                    processed_data = process_data(response.json())
                    success_count += 1
                    break
                else:
                    print("Taking a break")
                    time.sleep(2)
            print(url)
        finally:
            data_blob.append(processed_data)

    print("Success_count: {0}".format(success_count))
    print("fail_count: {0}".format(fail_count))
    return data_blob

    


    

if __name__ == "__main__":

    # todo : dont need to save all party information, maybe just shorthand is enough
    print("Filter parties")
    # selected_parties = filter_parties()    

    # party_key will identify party in Ridings api calls || can make a dict of this
    print("Generate Party Keys")
    # party_keys = [party["ShortName_En"] for party in selected_parties]

    print("Find all ridings")
    total_ridings = find_all_ridings()

    # contains info for table 1
    print("Collecting Data")
    riding_info = get_riding_info(total_ridings)

    
    # riding_info = get_riding_info(100)


    print(time.time()-start)
    input()    









    
