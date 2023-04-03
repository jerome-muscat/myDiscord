CREATE TABLE `Categorie` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nom` INT NOT NULL,
  `id_room` INT NOT NULL,
  `id_user` INT NOT NULL
);

CREATE TABLE `Salon` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nom` TEXT NOT NULL,
  `id_message` INT NOT NULL
);

CREATE TABLE `Utilisateur` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nom` TEXT NOT NULL,
  `prenom` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  `mdp` TEXT NOT NULL,
  `pseudo` TEXT NOT NULL,
  `age` INT NOT NULL,
  `id_privilege` INT NOT NULL
);

CREATE TABLE `Message` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `text` TEXT NOT NULL,
  `id_utilisateur` INT NOT NULL,
  `date` DATETIME NOT NULL
);

CREATE TABLE `Privilege` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nom` ENUM('Proprietaire', 'admin', 'membre')
);

ALTER TABLE `Salon` ADD FOREIGN KEY (`id`) REFERENCES `Categorie` (`id_room`);

ALTER TABLE `Categorie` ADD FOREIGN KEY (`id_user`) REFERENCES `Utilisateur` (`id`);

ALTER TABLE `Message` ADD FOREIGN KEY (`id`) REFERENCES `Salon` (`id_message`);

ALTER TABLE `Utilisateur` ADD FOREIGN KEY (`id_privilege`) REFERENCES `Privilege` (`id`);

ALTER TABLE `Message` ADD FOREIGN KEY (`id_utilisateur`) REFERENCES `Utilisateur` (`id`);
