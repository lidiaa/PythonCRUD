CREATE DATABASE python_crud;




USE python_crud;




CREATE TABLE paises(
   id_pais int unsigned not null auto_increment,
   nome_pais varchar(45) not null,
   qtd_titulos int unsigned not null,
   PRIMARY KEY (id_pais)
);





INSERT INTO paises (nome_pais, qtd_titulos) VALUES ("Brasil",5);
INSERT INTO paises (nome_pais, qtd_titulos) VALUES ("Itália",4);
INSERT INTO paises (nome_pais, qtd_titulos) VALUES ("Alemanha",4);



