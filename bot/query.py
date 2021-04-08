import sqlite3


def query(query: str):
    con = sqlite3.connect('chinook.db')

    cur = con.cursor()

    # Insert a row of data
    cur.execute("select * from " + query)

    # Save (commit) the changes
    con.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    
    return cur.fetchall()
