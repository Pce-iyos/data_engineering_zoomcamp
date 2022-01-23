#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse


def main(params):
    user= params.user
    password= params.password
    host= params.host
    port= params.port
    dbname= params.dbname
    table_name=params.table_name
    url= params.url


    csv_name= 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine =create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')


    yellow_iter = pd.read_csv(csv_name,iterator=True, chunksize=100000 )

    yell_car = next(yellow_iter)

    yell_car.tpep_pickup_datetime= pd.to_datetime(yell_car['tpep_pickup_datetime'])
    yell_car.tpep_dropoff_datetime= pd.to_datetime(yell_car.tpep_dropoff_datetime)
        

    yell_car.head(0).to_sql(name= table_name, con= engine, if_exists='replace')

    yell_car.to_sql(name= table_name, con= engine, if_exists='append')

    while True:
        t_start= time()
        
        yell_car = next(yellow_iter)
        yell_car.tpep_pickup_datetime= pd.to_datetime(yell_car['tpep_pickup_datetime'])
        yell_car.tpep_dropoff_datetime= pd.to_datetime(yell_car.tpep_dropoff_datetime)
        
        
        yell_car.to_sql(name= table_name, con= engine, if_exists='append')
        
        t_end = time()
        
        print('inserting another chunk, took %.3f seconds' %(t_end - t_start))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingesting Data with python ')



    parser.add_argument('--user',help='username of postgres')
    parser.add_argument('--password',help='password of postgres')
    parser.add_argument('--host',help='host of postgres')
    parser.add_argument('--port',help='port of postgres')
    parser.add_argument('--dbname',help='dbname of postgres')
    parser.add_argument('--table_name',help='table name of postgres')
    parser.add_argument('--url',help='url for csvfile ')
    # parser.add_argument('integers',help='an integer for the accumulator')

    args = parser.parse_args()

    main(args)


