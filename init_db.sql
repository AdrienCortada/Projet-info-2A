SET SEARCH_PATH = projet ;

DROP TABLE IF EXISTS type CASCADE ;
DROP TABLE IF EXISTS modality CASCADE ;
DROP TABLE IF EXISTS metatype CASCADE ;
DROP TABLE IF EXISTS donnee CASCADE ;

CREATE TABLE type(
    id_type integer PRIMARY KEY,
    nom_type text,
    taux_remplissage float
);
CREATE TABLE modality (
    id_modality integer PRIMARY KEY,
    id_type integer REFERENCES type(id_type),
    value text,
    proba float
);

CREATE TABLE metatype(
    id_metatype integer PRIMARY KEY,
    id_type integer REFERENCES type(id_type),
    nom_metatype text
);

CREATE TABLE donnee(
    id_donnee integer PRIMARY KEY,
    id_type integer REFERENCES type(id_type),
    value_donnee text,
    ordre integer,
    id_metatype integer REFERENCES metatype(id_metatype)
);

INSERT INTO type(id_type, nom_type, taux_remplissage) VALUES
(1, 'sexe', 1),
(2, 'prénom', 1);

INSERT INTO modality(id_modality, id_type, value) VALUES
(1, 1, 'femme'),
(2, 1, 'homme'),
(3, 2, 'Laurène'),
(4, 2, 'Isaac'),
(5, 2, 'Adrien');
