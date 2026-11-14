DROP TABLE IF EXISTS Salesman;
CREATE TABLE IF NOT EXISTS Salesman(
    salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission TEXT
);
INSERT INTO Salesman(salesman_id,name,city,commission)
VALUES
("5001","James Hoog","New York","0.15"),
("5002","Nail Knite","Paris","0.13"),
("5005","Pit Alex","London","0.11"),
("5006","Mc Lyon","Paris","0.14"),
("5007","Paul Adam","Rome","0.13"),
("5003","Lauson Hen","San Jose","0.12");

DROP TABLE IF EXISTS Customer;
CREATE TABLE IF NOT EXISTS Customer(
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    salesman_id TEXT
);

INSERT INTO Customer(customer_id,cust_name,city,grade,salesman_id)
VALUES
("3002","nick rimando","new york","100","5001"),
("3007","brad davis","new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabian johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"),
("3001","brad guzan","london","","5005");

DROP TABLE IF EXISTS Orders;
CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);

INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,salesman_id)
VALUES
("3002","nick rimando","new york","100","5001"),
("3007","brad davis","new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabian johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"),
("3001","brad guzan","london","","5005");

SELECT * FROM Salesman;
SELECT * FROM Customer;
SELECT * FROM Orders;

SELECT Customer.cust_name, Salesman.name, Salesman.city
FROM Customer
JOIN Salesman ON Customer.city = Salesman.city;
