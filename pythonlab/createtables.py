import psycopg2

def makeTables():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    
    cur = conn.cursor()
    
    # Make the cities table:
    makeCities = """
        CREATE TABLE us_cities (
            city text,
            home_state text,
            city_pop integer,
            lat real,
            lon real
        );
    """   
    cur.execute("DROP TABLE IF EXISTS us_cities CASCADE;")
    cur.execute(makeCities)
    
    makeStates = """
        CREATE TABLE us_states (
            code char(2),
            state text,
            state_pop integer 
        );
    """
    cur.execute("DROP TABLE IF EXISTS us_states CASCADE;")
    cur.execute(makeStates)
    
    conn.commit()    

    
if __name__ == "__main__":
    makeTables()