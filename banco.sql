-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8 ;
USE `biblioteca` ;

-- -----------------------------------------------------
-- Table `biblioteca`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`usuario` (
  `nome` VARCHAR(100) NOT NULL,
  `user` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(255) NOT NULL,
  `admin` INT NULL,
  `email` VARCHAR(255) NULL,
  PRIMARY KEY (`user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `cep` INT NOT NULL,
  `endereco` VARCHAR(255) NULL,
  `numero` VARCHAR(20) NULL,
  `bairro` VARCHAR(55) NULL,
  `cidade` VARCHAR(55) NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `isbn_10` VARCHAR(45) NOT NULL,
  `isbn_13` VARCHAR(45) NOT NULL,
  `titulo` VARCHAR(50) NOT NULL,
  `autor` VARCHAR(55) NOT NULL,
  `lancamento` DATE NOT NULL,
  `sinopse` VARCHAR(5000) NOT NULL,
  `quantidade` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`emprestimo` (
  `id_emprestimo` INT NOT NULL AUTO_INCREMENT,
  `data_saida` DATE NULL,
  `data_retorno` DATE NULL,
  `cliente_id_cliente` INT NOT NULL,
  `livro_id` INT NOT NULL,
  PRIMARY KEY (`id_emprestimo`, `cliente_id_cliente`, `livro_id`),
  INDEX `fk_emprestimo_cliente_idx` (`cliente_id_cliente` ASC) VISIBLE,
  INDEX `fk_emprestimo_livro1_idx` (`livro_id` ASC) VISIBLE,
  CONSTRAINT `fk_emprestimo_cliente`
    FOREIGN KEY (`cliente_id_cliente`)
    REFERENCES `biblioteca`.`cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emprestimo_livro1`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO usuario (nome, user, senha, admin, email) VALUES ("admin", "admin", "$2b$12$ewe26n9QJ81wHv4WFV/JqOikDYN/jRn/cyJsWYuhKjCZzHExy6PTa", 1, "admin@admin.com");

INSERT INTO livro (isbn_10, isbn_13, titulo, autor, lancamento, sinopse, quantidade) 
VALUES ("853253080X", "9788532530806", "Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", 2017-08-19, "As aulas estão de volta à Hogwarts e Harry Potter não vê a hora de embarcar no expresso a vapor que o levará de volta à escola de bruxaria. Mais uma vez suas férias na rua dos Alfeneiros foi triste e solitária. Com muita ação, humor e magia, 'Harry Potter e o prisioneiro de Azkaban' traz de volta o gigante atrapalhado Rúbeo Hagrid, o sábio diretor Alvo Dumbledore, a exigente professora de transformação Minerva MacGonagall e o novo mestre Lupin, que guarda grandes surpresas para Harry.", 3);

INSERT INTO cliente (nome, cpf, cep, endereco, numero, bairro, cidade, telefone, email) 
VALUES
('Carlos Mago',
'58935874839',
06578118,
'Rua Abel Ferreira',
345,
'Jd. Palestra',
'São Pauo-SP',
'11967456747',
'carlosmago@classedenewbie.com');


INSERT INTO emprestimo (data_saida, data_retorno, cliente_id_cliente, livro_id) VALUES ('2024-03-05', '2024-03-10', 1, 1);




