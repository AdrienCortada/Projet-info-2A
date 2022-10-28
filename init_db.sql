-- SET SEARCH_PATH = projet ;

DROP TABLE IF EXISTS type CASCADE ;
DROP TABLE IF EXISTS modality CASCADE ;
DROP TABLE IF EXISTS metatype CASCADE ;
DROP TABLE IF EXISTS donnee CASCADE ;
DROP SEQUENCE IF EXISTS id_modality_seq ;

CREATE SEQUENCE id_modality_seq ; 

CREATE TABLE type(
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
('prénom', 1);

INSERT INTO modality(nom_type, value) VALUES
('sexe', 'femme'),
('sexe', 'homme'),
('prénom', 'Laurène'),
('prénom', 'Isaac'),
('prénom', 'Adrien'),
('prénom', 'Laurène'),
('prénom', 'Laurène'),
('prénom', 'Laurène');
