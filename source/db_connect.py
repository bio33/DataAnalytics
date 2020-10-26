import psycopg2
from psycopg2.extras import execute_batch
import configparser
import os




def get_connection(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    db_username = config['postgresql']['USERNAME']
    db_pw = str(config['postgresql']['PASSWORD'])
    db_host = str(config['postgresql']['HOST'])
    db_port = str(config['postgresql']['PORT'])
    db_DB = str(config['postgresql']['DB'])

    engine = psycopg2.connect(
            database = db_DB,
            user = db_username,
            password = db_pw,
            host = db_host,
            port = db_port
    )

    return engine

def create_tables(conn):
    try:
        commands = (
            """DROP TABLE IF EXISTS vote_share2 cascade;""",
            """ 
                CREATE TABLE vote_share2(
                RidingNumber INTEGER PRIMARY KEY,
                RidingName_En VARCHAR(255) NOT NULL,
                RidingName_Fr VARCHAR(255) NOT NULL,
                TotalVotes INTEGER NOT NULL,
                TurnOut DECIMAL ,
                CON DECIMAL ,
                LIB DECIMAL ,
                NDP DECIMAL ,
                GRN DECIMAL ,
                BQ DECIMAL ,
                PPC DECIMAL
            ); """,
            """DROP TABLE IF EXISTS candidates2; """,
            """ 
            CREATE TABLE candidates2(
                RidingNumber INTEGER PRIMARY KEY,
                LIB  VARCHAR(255),
                NDP  VARCHAR(255),
                CON  VARCHAR(255),
                GRN  VARCHAR(255),
                BQ VARCHAR(255),
                PPC VARCHAR(255),
                FOREIGN KEY (RidingNumber)
                    REFERENCES vote_share2(RidingNumber)
            );"""
            )
        
        cur = conn.cursor()

        
        for command in commands :
            cur.execute(command)
        print("Tables created")
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return 0

def load_data(conn,data,table_name):
    cur = conn.cursor()
    try:
        
        if table_name == "vote_share2":
            sql = """INSERT INTO vote_share2 values (%(RidingNumber)s, %(RidingName_En)s,%(RidingName_Fr)s,%(TotalVotes)s,%(TurnOut)s,%(CON)s,%(LIB)s,%(NDP)s,%(GRN)s,%(BQ)s,%(PPC)s);"""
        elif table_name == "candidates2":
            sql = """INSERT INTO candidates2 values (%(RidingNumber)s, %(LIB)s,%(NDP)s,%(CON)s,%(GRN)s,%(BQ)s,%(PPC)s);"""
        else:
            print("Bad table name")
            return 1
        # execute_batch(cur, vote_share_sql, vote_share_data, page_size=1000)
        execute_batch(cur, sql, data, page_size=1000)
        print("data uploaded")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.commit()
        return 0
    
def query_table(conn):
    sql = "Select * from vote_share2"
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    return 0

if __name__ == '__main__':
    config_file_path = os.getcwd() + r"\creds\local_creds.ini"
    conn = get_connection(config_file_path)
    # cur = conn.cursor()
    # cur.execute('Select version()')
    # version = cur.fetchone()[0]
    # print(version)
    # create_tables(conn)
    # load_data
    query_table(conn)
    conn.close()

