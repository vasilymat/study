SELECT users.email, SUM(transactions.price) AS Price
FROM users
JOIN transactions
ON users.user_id = transactions.user_id
WHERE users.user_id IN (
SELECT user_id FROM users 
	JOIN webinar ON users.email = webinar.email
	WHERE users.email NOT IN 
	(SELECT email FROM users WHERE users.date_reg < '2016-04-01 00:00:00')
)
GROUP BY users.email;

/*
SELECT users.email, SUM(transactions.price) AS SUMM FROM users JOIN transactions ON users.user_id=transactions.user_id WHERE users.user_id IN 
(SELECT user_id FROM users JOIN webinar ON users.email = webinar.email WHERE users.email NOT IN 
(SELECT email FROM users WHERE date_reg < '2016-04-01 00:00:00' ) );
*/
/*SELECT users.user_id--, users.email, users.date_reg
FROM users
JOIN webinar
ON users.email = webinar.email
WHERE users.email NOT IN (SELECT email FROM users WHERE users.date_reg < '2016-04-01 00:00:00');



ON users.email = webinar.email
JOIN transactions
ON transactions.user_id = users.user_id
WHERE users.email NOT IN (SELECT email FROM users WHERE users.date_reg < '2016-04-01 00:00:00')
*/