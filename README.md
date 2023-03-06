# PROYECTO INDIVIDUAL CODING DOJO
Este proyecto fue desarrollado en flask a partir de los conocimientos adquieridos a través del bootcamp de Coding Dojo.

Se recomienda seguir los siguientes pasos:
1. Crear carpeta en la cual quieres albergar el proyect.
2. Abrir la carpeta en la terminar de Visual Studio.
3. Crear el ambiente virtual.
4. Instalar flask, flask-bcrypt
5. Instalar pymsql
3. Crear todas las carpetas correspondientes
4. Crear todos los archivos .py
5. Crear todos los archivos .html
6. Copiar y pegar el contenido en el archivo correspondiente

## Para crear la base de datos
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `solo_project` DEFAULT CHARACTER SET utf8 ;
USE `solo_project` ;

-- -----------------------------------------------------
-- Table `solo_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `solo_project`.`users` (
  `idUsers` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `company` VARCHAR(45) NULL DEFAULT NULL,
  `department` VARCHAR(45) NULL DEFAULT NULL,
  `position` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `password` VARCHAR(500) NULL DEFAULT NULL,
  `available` TINYINT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idUsers`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `solo_project`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `solo_project`.`products` (
  `idProducts` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(300) NULL DEFAULT NULL,
  `project` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `date_start` DATE NULL DEFAULT NULL,
  `date_finished` DATETIME NULL DEFAULT NULL,
  `deadline` DATE NULL DEFAULT NULL,
  `finished` TINYINT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`idProducts`),
  INDEX `fk_products_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `solo_project`.`users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `solo_project`.`chores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `solo_project`.`chores` (
  `idChores` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL DEFAULT NULL,
  `description` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `finished_at` DATETIME NULL DEFAULT NULL,
  `finished` TINYINT NULL DEFAULT NULL,
  `product_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`idChores`),
  INDEX `fk_chores_projects1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_chores_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_chores_projects1`
    FOREIGN KEY (`product_id`)
    REFERENCES `solo_project`.`products` (`idProducts`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chores_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `solo_project`.`users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
