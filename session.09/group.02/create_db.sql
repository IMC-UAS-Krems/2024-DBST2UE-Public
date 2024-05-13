CREATE TABLE Person (
	name VARCHAR(255),
	age UNSIGNED INT NOT NULL CHECK (age > 0 AND age < 130),
	gender CHAR CHECK (gender IN ("M", "F", "O", "m", "f", "o")),
	PRIMARY KEY(name)
);

CREATE TABLE Frequents (
	name VARCHAR(255) NOT NULL,
	pizzeria VARCHAR(255) NOT NULL,
	PRIMARY KEY(name, pizzeria),
	FOREIGN KEY (name) REFERENCES Person(name)	
);

CREATE TABLE Eats(
	name VARCHAR(255) NOT NULL,
	pizza VARCHAR(255) NOT NULL,
	PRIMARY KEY(name, pizza),
	FOREIGN KEY (name) REFERENCES Person(name)
);

CREATE TABLE Serves(
	pizzeria VARCHAR(255) NOT NULL,
	pizza VARCHAR(255) NOT NULL,
	price NUMERIC(10,2) NOT NULL CHECK (price > 0),
	PRIMARY KEY(pizzeria, pizza)
);
