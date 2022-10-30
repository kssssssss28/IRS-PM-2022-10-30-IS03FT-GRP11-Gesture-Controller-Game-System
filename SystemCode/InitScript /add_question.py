import pymysql
import argparse
def add_question(que,A,B,C,D,ANS):

    db = pymysql.connect(host='localhost',
                        user='root',
                        password='12345678',
                        database='QUESTIONS')

    cursor = db.cursor()
    cursor.execute('CREATE DATABASE QUESTIONS')
    ## defining the Query
    sql = 'SELECT * FROM QUESTIONS_tbl'
    cursor.execute(sql)
    questions = cursor.fetchall()
    count = len(questions)
     ## defining the Query
    query ="INSERT INTO QUESTIONS_tbl VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (count+1, que, A, B, C, D, ANS)
 
     ## executing the query with values
    cursor.execute(query, values)
    db.commit()

def get_args():
    parser = argparse.ArgumentParser(description='Add questions to the database.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('question',  type=str, 
                        help='The question to be added')
    parser.add_argument('A', type=str,
                        help='Choice A')
    parser.add_argument('B', type=str,
                        help='Choice B')
    parser.add_argument('C', type=str,
                        help='Choice C')
    parser.add_argument('D', type=str,
                        help='Choice D')  
    parser.add_argument('ans', type=str,
                        help='The correct answer')                   


    return parser.parse_args()


if __name__  == '__main__':
    args = get_args()
    add_question(args.question, args.A, args.B, args.C, args.D, args.ans)
    print('Add successfully!!')
