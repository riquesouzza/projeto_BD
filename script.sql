SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `passagem`;
DROP TABLE IF EXISTS `viagem`;
DROP TABLE IF EXISTS `linhaPontos`;
DROP TABLE IF EXISTS `horariosLinha`;
DROP TABLE IF EXISTS `linha`;
DROP TABLE IF EXISTS `onibus`;
DROP TABLE IF EXISTS `cobrador`;
DROP TABLE IF EXISTS `motorista`;
DROP TABLE IF EXISTS `cartaoTransporte`;
DROP TABLE IF EXISTS `pontoOnibus`;
DROP TABLE IF EXISTS `empresa`;
DROP TABLE IF EXISTS `passageiro`;
SET FOREIGN_KEY_CHECKS = 1;

-- Tabelas

CREATE TABLE `passageiro` (
  `CPF` varchar(255) PRIMARY KEY,
  `nome` varchar(255) NOT NULL,
  `telefone` varchar(255),
  `email` varchar(255) NOT NULL,
  `dataNascimento` date NOT NULL
);

CREATE TABLE `empresa` (
  `CNPJ` varchar(255) PRIMARY KEY,
  `telefone` varchar(255),
  `nome` varchar(255) NOT NULL,
  `endereco` varchar(255) 
);

CREATE TABLE `pontoOnibus` (
  `codPonto` integer PRIMARY KEY AUTO_INCREMENT,
  `endereco` varchar(255) NOT NULL
);

CREATE TABLE `cartaoTransporte` (
  `id` integer PRIMARY KEY,
  `Usuario` varchar(255) UNIQUE,
  `saldo` float NOT NULL,
  FOREIGN KEY (`Usuario`) REFERENCES `passageiro` (`CPF`)
);

CREATE TABLE `motorista` (
  `CNH` varchar(255) PRIMARY KEY,
  `nome` varchar(255) NOT NULL,
  `telefone` varchar(255),
  `jornada` integer NOT NULL
);

CREATE TABLE `cobrador` (
  `matricula` varchar(255) PRIMARY KEY,
  `nome` varchar(255) NOT NULL,
  `telefone` varchar(255),
  `escala` integer NOT NULL
);

CREATE TABLE `onibus` (
  `placa` varchar(255) PRIMARY KEY,
  `capacidade` integer,
  `idEmpresa` varchar(255) NOT NULL,
  FOREIGN KEY (`idEmpresa`) REFERENCES `empresa` (`CNPJ`)
);

CREATE TABLE `linha` (
  `codLinha` integer PRIMARY KEY,
  `idEmpresa` varchar(255),
  `nome` varchar(255) NOT NULL,
  FOREIGN KEY (`idEmpresa`) REFERENCES `empresa` (`CNPJ`)
);

CREATE TABLE `horariosLinha` (
  `idLinha` integer,
  `horario` time,
  PRIMARY KEY (`idLinha`, `horario`),
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`)
);

CREATE TABLE `linhaPontos` (
  `idLinha` integer,
  `codPonto` integer,
  PRIMARY KEY (`idLinha`, `codPonto`),
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`),
  FOREIGN KEY (`codPonto`) REFERENCES `pontoOnibus` (`codPonto`)
);

CREATE TABLE `viagem` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `motorista` varchar(255) NOT NULL,
  `cobrador` varchar(255),
  `placa` varchar(255) NOT NULL,
  `idLinha` integer NOT NULL,
  `horaChegada` time NOT NULL,
  `horaSaida` time NOT NULL,
  `data` date NOT NULL,
  FOREIGN KEY (`placa`) REFERENCES `onibus` (`placa`),
  FOREIGN KEY (`motorista`) REFERENCES `motorista` (`CNH`),
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`),
  FOREIGN KEY (`cobrador`) REFERENCES `cobrador` (`matricula`)
);

CREATE TABLE `passagem` (
  `id` integer PRIMARY KEY,
  `numCartao` integer NOT NULL,
  `valor` float NOT NULL,
  `dataHora` datetime,
  `idViagem` integer NOT NULL,
  FOREIGN KEY (`numCartao`) REFERENCES `cartaoTransporte` (`id`),
  FOREIGN KEY (`idViagem`) REFERENCES `viagem` (`id`)
);

DELIMITER $$

CREATE PROCEDURE registrar_passagem(
    IN p_numCartao INT,
    IN p_valor FLOAT,
    IN p_idViagem INT
)
BEGIN
    DECLARE v_saldo FLOAT;
    DECLARE novoId INT;

    -- Busca o saldo atual do cartão
    SELECT saldo INTO v_saldo
    FROM cartaoTransporte
    WHERE id = p_numCartao;

    -- Verifica se o cartão existe
    IF v_saldo IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cartão inexistente.';
    END IF;

    -- Verifica se tem saldo suficiente
    IF v_saldo < p_valor THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Saldo insuficiente para realizar a passagem.';
    END IF;

    -- Gera ID manual (SEM AUTO_INCREMENT)
    SELECT IFNULL(MAX(id), 0) + 1 INTO novoId FROM passagem;

    -- Insere a passagem com ID manual
    INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem)
    VALUES (
        novoId,
        p_numCartao,
        p_valor,
        NOW(),
        p_idViagem
    );

    -- Atualiza o saldo do cartão
    UPDATE cartaoTransporte
    SET saldo = saldo - p_valor
    WHERE id = p_numCartao;

END $$

DELIMITER ;
