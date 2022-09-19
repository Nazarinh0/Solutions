--OLD TABLE
CREATE TABLE old_cars (
    model varchar(255),
    brand varchar(255),
    price integer,
    discount integer,
    PRIMARY KEY (model, brand)
);

INSERT INTO old_cars VALUES
('m5', 'bmw', 5500000, 5),
('x5m', 'bmw', 6000000, 5),
('m1', 'bmw', 2500000, 5),
('almera', 'nissan', 5500000, 10),
('gt-r', 'nissan', 5000000, 10);

-- END OF OLD TABLE


CREATE TABLE brands (
    id bigint PRIMARY KEY,
    name varchar(255),
    discount int
);

CREATE TABLE cars (
    id bigint PRIMARY KEY,
    brand_id bigint REFERENCES brands (id),
    model varchar(255),
    price numeric
);

INSERT INTO brands VALUES
(1, 'bmw', 5),
(2, 'nissan', 10);

INSERT INTO cars VALUES
(1, 1, 'm5', 5500000),
(2, 1, 'x5m', 6000000),
(3, 1, 'm1', 2500000),
(4, 2, 'almera', 5500000),
(5, 2, 'gt-r', 5000000);

