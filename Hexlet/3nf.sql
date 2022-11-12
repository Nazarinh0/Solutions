-- OLD TABLE
CREATE TABLE old_cities (
    country varchar(255),
    region varchar(255),
    city varchar(255)
);

INSERT INTO old_cities VALUES
('Россия', 'Татарстан', 'Бугульма'),
('Россия', 'Самарская область', 'Тольятти'),
('Россия', 'Татарстан', 'Казань');

CREATE TABLE countries (
    id bigint PRIMARY KEY,
    name varchar(255)
);
-- END OF OLD TABLE


CREATE TABLE country_regions (
    id bigint PRIMARY KEY,
    country_id bigint REFERENCES countries (id),
    name varchar(255)
);

CREATE TABLE country_region_cities (
    id bigint PRIMARY KEY,
    country_region_id bigint REFERENCES country_regions (id),
    name varchar(255)
);

INSERT INTO countries VALUES (1, 'Россия');
INSERT INTO country_regions VALUES
(1, 1, 'Татарстан'),
(2, 1, 'Самарская область');
INSERT INTO country_region_cities VALUES
(1, 1, 'Казань'),
(2, 1, 'Бугульма'),
(3, 2, 'Тольятти');
