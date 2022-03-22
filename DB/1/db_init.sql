CREATE TABLE users(
    id SERIAL,
    user_id  INTEGER,
    email    VARCHAR(255),
    date_reg TIMESTAMP,
    PRIMARY KEY (id)
);

COPY users (user_id,email,date_reg)
FROM 'C:/MatkivskiyV/study/DB/1/users.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE webinar(
	id SERIAL,
	email VARCHAR(255),
	PRIMARY KEY (id)
);

COPY webinar (email)
FROM 'C:/MatkivskiyV/study/DB/1/webinar.csv'
CSV HEADER;

CREATE TABLE transactions(
    id SERIAL,
	user_id INTEGER,
	price   REAL,
	PRIMARY KEY (id)
);

COPY transactions (user_id,price)
FROM 'C:/MatkivskiyV/study/DB/1/transactions.csv'
DELIMITER ','
CSV HEADER;