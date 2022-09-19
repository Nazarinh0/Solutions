CREATE TABLE users (
    id bigint PRIMARY KEY,
    first_name varchar(255),
    created_at timestamp
);

INSERT INTO users VALUES (1, 'Tom', '2022-05-24');

CREATE TABLE orders(
    id bigint PRIMARY KEY,
    user_first_name varchar(255),
    months int,
    created_at timestamp
);

INSERT INTO orders VALUES
(1, 'Tom', 2, '2022-09-19'),
(2, 'Tom', 4, '2022-05-25');

