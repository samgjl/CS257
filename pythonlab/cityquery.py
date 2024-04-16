import psycopg2

def getConnection():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    if not conn:
        print("Oops, we don't have a connection!")
        exit(1)
        
    cur = conn.cursor()
    return conn, cur

def queries():
    conn, cur = getConnection()
    
    # Northfield:
    print("1. Looking for Northfield, MN...")
    cur.execute("""SELECT * FROM us_cities WHERE city LIKE 'Northfield';""")
    northfield = cur.fetchone()
    
    if northfield:
        print(f"   Northfield location:\n    LAT: {northfield[3]}\n    LONG: {northfield[4]}\n")
    else:
        print("   Northfield is not in this dataset.\n")
        
    # Largest city:
    largeQuery = """
        SELECT * FROM us_cities
        ORDER BY 
            city_pop
        DESC;"""
    
    print("2. What's the largest US city in this dataset?")
    cur.execute(largeQuery)
    largeResult = cur.fetchone()
    print(f"""   It's {largeResult[0]}! Its population is  {largeResult[2]}, at {largeResult[3]} degrees North by {-1*largeResult[4]} degrees West.\n""")
    
    # Smallest MN city:
    smallMNQuery = """
        SELECT * FROM us_cities
        WHERE 
            home_state LIKE 'Minnesota'
        ORDER BY 
            city_pop 
        ASC;
    """
    print("3. What's the smallest city in this dataset located in MN?")    
    cur.execute(smallMNQuery)
    smallMNResult = cur.fetchone()
    print(f"""   It's {smallMNResult[0]}! Its population is  {smallMNResult[2]}, at {smallMNResult[3]} degrees North by {-1*smallMNResult[4]} degrees West.\n""")  
    
    # N S E W
    cur.execute("SELECT * FROM us_cities ORDER BY lat DESC;")
    ns = cur.fetchall()
    cur.execute("SELECT * FROM us_cities ORDER BY lon DESC;")
    ew = cur.fetchall()
    
    print("4. In this dataset, the furthest cities in each cardinal direction are as follows:")
    print(f"    Furthest North: {ns[0][0]}, {ns[0][1]}.")
    print(f"    Furthest South: {ns[-1][0]}, {ns[-1][1]}.")
    print(f"    Furthest East: {ew[0][0]}, {ew[0][1]}.")
    print(f"    Furthest West: {ew[-1][0]}, {ew[-1][1]}.")
    print("")
    
      
    
def interactiveQueries():
    conn, cur = getConnection()
    # Input and cleaning:
    invalid = True
    while invalid:
        state = input("5. Please enter the name or 2-letter code of a state: ")
        column = "state"
        if len(state) == 2:
            column = "code"
        # Check if this is a real state
        cur.execute(f"SELECT * FROM us_states WHERE {column} LIKE '{state}' LIMIT 1;")
        state = cur.fetchone()
        if state:
            invalid = False
            state = state[1]
        else:
            print("Hmm... We couldn't find that state. Please try again.\n")
    
    # Fun printing:
    print(f"   You have selected {state}!")
    cur.execute(f"SELECT * FROM us_states WHERE state LIKE '{state}' LIMIT 1;")
    state_pop = cur.fetchone()[2]
    print(f"   {state}'s population overall is {state_pop}.")
    
    # Calculating the sum of all city populations in this state:
    cur.execute(f"SELECT * FROM us_cities WHERE home_state LIKE '{state}';")
    cities = cur.fetchall()
    city_sum = 0
    for city in cities:
        city_sum += city[2]
    print(f"   The populations of its {len(cities)} cities in this set sum to {city_sum}.")
    print(f"   That's {round(100 * city_sum / state_pop, 1)}% of the state's population (potential rounding errors).") # For fun!
    # ^ So DC actually has a pretty bad rounding erorr here...
    print("")
    
    
    

if __name__ == "__main__":
    queries()
    interactiveQueries()