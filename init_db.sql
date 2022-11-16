-- SET SEARCH_PATH = projet ;

DROP TABLE IF EXISTS type CASCADE ;
DROP TABLE IF EXISTS modality CASCADE ;
DROP TABLE IF EXISTS meta_type CASCADE ;
DROP TABLE IF EXISTS donnee CASCADE ;
DROP SEQUENCE IF EXISTS id_modality_seq ;
DROP SEQUENCE IF EXISTS id_type_seq ;
DROP SEQUENCE IF EXISTS id_meta_type_seq ;
DROP SEQUENCE IF EXISTS id_donnee_seq ;


CREATE SEQUENCE id_modality_seq ; 
CREATE SEQUENCE id_type_seq ;
CREATE SEQUENCE id_meta_type_seq ;
CREATE SEQUENCE id_donnee_seq ;

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

CREATE TABLE meta_type (
    id_meta_type INT PRIMARY KEY DEFAULT nextval('id_meta_type_seq'),
    nom_meta_type text,
	nom_type text REFERENCES type(nom)
);

CREATE TABLE donnee (
	id_donnee INT PRIMARY KEY DEFAULT nextval('id_donnee_seq'),
	--id_type INT REFERENCES type(id_type) DEFAULT NULL,
	id_meta_type INT REFERENCES meta_type(id_meta_type),
	value_donnee text,
	order_donnee int	
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

INSERT INTO meta_type(nom_meta_type, nom_type) VALUES
('individu', 'prénom'),
('individu', 'sexe'),
('commune', 'code postal'),
('commune', 'nom commune');

INSERT INTO donnee(id_meta_type, value_donnee, order_donnee) VALUES
(1, 'Laurène', 1),
(2, 'femme', 2),
(1, 'Nathan', 1),
(2, 'homme', 2),
(3, '35000', 1),
(4, 'Rennes', 2),
(3, '31000', 1),
(4, 'Toulouse', 2);
