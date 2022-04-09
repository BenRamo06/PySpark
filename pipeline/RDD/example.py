import sys
import json 
from pyspark import RDD, SparkContext
from pyspark.sql import SparkSession


from pipeline.RDD.dependencies import errorsClass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(""" We must use: <file_name>.py <number>""")
        sys.exit()
    else:

        def get_name(element, name_movies):

            cols = 'character,movie'.split(',')
            
            json_date = dict(zip(cols,element))

            json_date['name_movie'] = name_movies.get(json_date['movie'], "N/A")

            return json_date 



        file_name = sys.argv[1]
        
        session = SparkSession.builder.appName('"test RDD').getOrCreate()

        movies = json.loads('{"1":"Phantom menace","2":"Attack of clones", \
        "5" : "The Empire Strikes Back", \
        "6" : "Return of the Jedi", \
        "3" : "Revenge of the Sith", \
        "4" : "A new hope", \
        "7" : "The Force Awakens", \
        "8" : "The Last Jedi", \
        "9" : "The Rise of Skywalker"}')

        sc = session.sparkContext

        file = sc.textFile(file_name)

        get_data = file.map(lambda x: x.split(','))

        valid_row = get_data.filter(lambda x : len(x) == 2)

        get_json = valid_row.map(lambda x: get_name(element=x, name_movies=movies ))


        errorsClass('Entrooooooooooooooooooooooo')

        print(get_json.take(100))


        session.stop()