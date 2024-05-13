function setup_test(){
  # Load the Data - Assume 1 input
  cat <<EOT > $1
PRAGMA foreign_keys = 1;

INSERT INTO Person VALUES
('Annie', 20, 'F'),
('Bob', 20, 'M');

INSERT INTO Frequents VALUES
('Annie', 'Mammamia'),
('Annie', 'Gino'),
('Bob', 'Riva');

INSERT INTO Serves VALUES
('Mammamia', 'pepperoni', 10),
('Gino', 'pepperoni', 12),
('Riva', 'margherita', 8);

INSERT INTO Eats VALUES
('Annie', 'pepperoni'),
('Bob', 'pepperoni');
EOT
}

function setup_oracle(){
  # Setup the oracle
  cat <<EOT > $1
Annie
EOT
}