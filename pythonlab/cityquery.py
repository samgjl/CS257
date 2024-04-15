import psycopg2

def queries():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM us_cities WHERE city LIKE 'Northfield';""")
    northfield = cur.fetchone()
    
    if northfield:
        print(f"Northfield location:\n    LAT: {northfield[3]}\n    LONG: {northfield[4]}")
    else:
        print("Northfield is not in this dataset.")
        
    smallMNQuery = """
        SELECT * FROM us_cities
        WHERE 
            home_state LIKE 'MN'
        ORDER BY 
            city_pop 
        ASC;
    """
    cur.execute(smallMNQuery)
    smallMNQuery = cur.fetchone()
    print(smallMNQuery)
    
    



if __name__ == "__main__":
    queries()