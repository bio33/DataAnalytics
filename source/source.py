from data_collection import find_all_ridings,get_riding_info
from db_connect import get_connection,create_tables,load_data
import os
import time

def start():
    print("Find all ridings")
    total_ridings = find_all_ridings()

    print("Collecting Data")
    riding_info = get_riding_info(total_ridings)
    # print(riding_info)
    
    print("Connecting to DB")
    #local db
    # config_file_path = os.getcwd() + r"\creds\local_creds.ini"
    # prod db
    config_file_path = os.getcwd() + r"\creds\creds.ini"
    
    conn = get_connection(config_file_path)
    
    print("Creating Tables")
    create_tables(conn)
    
    print("Loading data into tables")
    vote_share_data = [record[0] for record in riding_info]
    candidate_data = [record[1] for record in riding_info]

    
    load_data(conn,vote_share_data,"vote_share2")
    print("Waiting for vote_share to load data")
    time.sleep(5)
    load_data(conn,candidate_data,"candidates2")

    conn.close()


if __name__ == '__main__':
    start()