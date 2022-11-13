-- SET SEARCH_PATH = projet ;

DROP TABLE IF EXISTS type CASCADE ;
DROP TABLE IF EXISTS modality CASCADE ;
DROP TABLE IF EXISTS metatype CASCADE ;
DROP TABLE IF EXISTS donnee CASCADE ;
DROP SEQUENCE IF EXISTS id_modality_seq ;
DROP SEQUENCE IF EXISTS id_type_seq ;
DROP SEQUENCE IF EXISTS id_metatype_seq ;


CREATE SEQUENCE id_modality_seq ; 
CREATE SEQUENCE id_type_seq ;
CREATE SEQUENCE id_metatype_seq ;

CREATE TABLE type (
    id_type INT DEFAULT nextval('id_type_seq'),
    nom text PRIMARY KEY,
    tx_remplissage float
);

CREATE TABLE modality (
	id_modality INT PRIMARY KEY DEFAULT nextval('id_modality_seq'),
    nom_type text REFERENCES type(nom),
    value text,
    proba_apparition float
);

INSERT INTO type(nom, tx_remplissage) VALUES
('sexe', 1),
('prénom', 1),
('code postal', 1),
('nom commune', 1);

INSERT INTO modality(nom_type, proba_apparition, value) VALUES
('sexe', 0.5, 'femme'),
('sexe', 0.5, 'homme');

INSERT INTO modality(nom_type, value) VALUES
('prénom', 'Laurène'),
('prénom', 'Isaac'),
('prénom', 'Adrien'),
('prénom', 'Laurène'),
('prénom', 'Laurène'),
('prénom', 'Laurène'),
('code postal', '31000'),
('code postal', '35000'),
('nom commune', 'Toulouse'),
('nom commune', 'Rennes');

CREATE TABLE metatype (
    id_metatype INT PRIMARY KEY DEFAULT nextval('id_metatype_seq'),
    nom_metatype text,
	nom_type text REFERENCES type(nom)
);

INSERT INTO metatype(nom_metatype, nom_type) VALUES
('individu', 'prénom'),
('individu', 'sexe'),
('commune', 'code postal'),
('commune', 'nom commune');
