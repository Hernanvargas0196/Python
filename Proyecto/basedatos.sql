CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE IF NOT EXISTS usuarios(
    id int(25) auto_increment not null,
    nombre VARCHAR(100),
    apellidos VARCHAR(255),
    email VARCHAR(255) not null,
    password VARCHAR(255) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)/*Campo unico*/
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo VARCHAR(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id) 
)ENGINE=InnoDB;
