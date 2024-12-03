def magic_eye(db_filename, *tools):
    import sqlite3
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    if not tools:
        return []

    placeholders = ','.join(['?'] * len(tools))
    query = f"""
    SELECT Events.witness, Magicians.magician, Places.place
    FROM Events
    JOIN Magicians ON Events.magician_id = Magicians.id
    JOIN Places ON Events.place_id = Places.id
    WHERE Magicians.tool IN ({placeholders})
    AND Events.outcome < 0
    """

    cursor.execute(query, tools)
    results = cursor.fetchall()

    results = sorted(results, key=lambda x: x[0], reverse=True)  # witness in reverse order
    results = sorted(results, key=lambda x: x[1])  # magician in normal order
    results = sorted(results, key=lambda x: x[2], reverse=True)  # place in reverse order

    conn.close()
    return results
