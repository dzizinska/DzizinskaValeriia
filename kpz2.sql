-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Owner`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Owner` (
  `idOwner` INT NOT NULL,
  `Owner_name` VARCHAR(45) NOT NULL,
  `FormOfOwnership` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idOwner`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Company` (
  `idCompany` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `Registration` DECIMAL NOT NULL,
  `Specification` MEDIUMTEXT NULL DEFAULT NULL,
  `Owner_idOwner` INT NOT NULL,
  PRIMARY KEY (`idCompany`, `Owner_idOwner`),
  INDEX `fk_Company_Owner1_idx` (`Owner_idOwner` ASC),
  CONSTRAINT `fk_Company_Owner1`
    FOREIGN KEY (`Owner_idOwner`)
    REFERENCES `mydb`.`Owner` (`idOwner`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ResponsiblePersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ResponsiblePersons` (
  `idResponsiblePersons` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `PasportCode` INT NOT NULL,
  `IdentificationCode` INT NOT NULL,
  PRIMARY KEY (`idResponsiblePersons`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`System_has_responsiblepersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`System_has_responsiblepersons` (
  `ResponsiblePersons_idResponsiblePersons` INT NOT NULL,
  `Company_idCompany` INT NOT NULL,
  PRIMARY KEY (`ResponsiblePersons_idResponsiblePersons`, `Company_idCompany`),
  INDEX `fk_System_has_responsiblepersons_Company1_idx` (`Company_idCompany` ASC),
  CONSTRAINT `fk_System_has_responsiblepersons_ResponsiblePersons`
    FOREIGN KEY (`ResponsiblePersons_idResponsiblePersons`)
    REFERENCES `mydb`.`ResponsiblePersons` (`idResponsiblePersons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_System_has_responsiblepersons_Company1`
    FOREIGN KEY (`Company_idCompany`)
    REFERENCES `mydb`.`Company` (`idCompany`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Licence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Licence` (
  `Licence_number` INT NOT NULL,
  `Series` VARCHAR(45) NOT NULL,
  `Issue_date` DATE NOT NULL,
  `Company_idCompany` INT NOT NULL,
  PRIMARY KEY (`Licence_number`, `Company_idCompany`),
  INDEX `fk_Licence_Company1_idx` (`Company_idCompany` ASC),
  CONSTRAINT `fk_Licence_Company1`
    FOREIGN KEY (`Company_idCompany`)
    REFERENCES `mydb`.`Company` (`idCompany`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
