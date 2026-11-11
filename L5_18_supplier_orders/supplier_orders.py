import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE orders (id INTEGER PRIMARY KEY, supplier TEXT, item TEXT, quantity INTEGER, received INTEGER, remarks TEXT)"
)
order_total = 0


def placeOrder(conn, supplier, item, quantity):
    global order_total
    if quantity < 0:
        raise ValueError("Quantity must be non-negative")

    conn.execute(
        "INSERT INTO orders (supplier, item, quantity, received, remarks) VALUES (?, ?, ?, 0, NULL)",
        (supplier, item, quantity),
    )
    conn.commit()
    order_total += quantity
    return order_total


def markReceived(conn, order_id, remarks):
    conn.execute(
        "UPDATE orders SET received = 1, remarks = ? WHERE id = ?",
        (remarks, order_id),
    )
    conn.commit()


def notifyWarehouse(supplier):
    print(f"notifying warehouse about {supplier}")


def cleanup(conn):
    conn.execute("DELETE FROM orders WHERE received = 1")
    conn.commit()


def pendingCount(conn):
    return conn.execute("SELECT COUNT(*) FROM orders WHERE received = 0").fetchone()[0]


def main():
    placeOrder(conn, "Acme Steel", "rods", 40)
    placeOrder(conn, "Bolt Co", "bolts", 500)
    markReceived(conn, 1, "ok")
    notifyWarehouse("Acme")
    print(pendingCount(conn), order_total)
    cleanup(conn)


if __name__ == "__main__":
    main()
