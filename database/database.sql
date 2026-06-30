CREATE DATABASE IF NOT EXISTS techsecure;

USE techsecure;

CREATE TABLE IF NOT EXISTS filiales (

    id INT AUTO_INCREMENT PRIMARY KEY,

    ville VARCHAR(100) NOT NULL,

    adresse VARCHAR(255) NOT NULL,

    responsable VARCHAR(100) NOT NULL,

    employes INT NOT NULL,

    ip_routeur VARCHAR(20) NOT NULL

);