import pymysql
import argparse


def init_DB(password):
    db = pymysql.connect(host='localhost',
                        user='root',
                        password=password
                        
                        )
    cursor = db.cursor()
    #cursor.execute('CREATE DATABASE QUESTIONS') 
    print('====== Database Created Successfully ======')
    cursor.execute("USE QUESTIONS")
    cursor.execute('CREATE TABLE IF NOT EXISTS QUESTIONS_tbl( question_id VARCHAR(100) NOT NULL,question VARCHAR(100) NOT NULL,A VARCHAR(255) NOT NULL, B VARCHAR(255) NOT NULL,C VARCHAR(255) NOT NULL,D VARCHAR(255) NOT NULL, ANS VARCHAR(255) NOT NULL,  PRIMARY KEY ( question_id ));')  
    query = open("QUESTIONS_tbl.sql", "r")
    sql = query.readlines()

    for i in sql:
        cursor.execute(i)
    
    db.commit()






def get_args():
    parser = argparse.ArgumentParser(description='Add questions to the database.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('password',  type=str, 
                        help='Password of the DB')                  
    return parser.parse_args()




if __name__  == '__main__':
    args = get_args()
    print('====== start to Init Database Successfully ======')
    init_DB(args.password)
    print('====== Init Database Successfully ======')
