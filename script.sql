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
DROP PROCEDURE IF EXISTS `registrar_passagem`;
DROP VIEW IF EXISTS `viagem_envolvidos`;
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
  `escala` integer NOT NULL,
  `foto` mediumblob
);

CREATE TABLE `onibus` (
  `placa` varchar(255) PRIMARY KEY,
  `capacidade` integer,
  `idEmpresa` varchar(255) NOT NULL,
  FOREIGN KEY (`idEmpresa`) REFERENCES `empresa` (`CNPJ`)
);

CREATE TABLE `linha` (
  `codLinha` integer PRIMARY KEY,
  `idEmpresa` varchar(255) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `valor` float NOT NULL,
  FOREIGN KEY (`idEmpresa`) REFERENCES `empresa` (`CNPJ`)
);


CREATE TABLE `horariosLinha` (
  `idLinha` integer,
  `horario` time,
  PRIMARY KEY (`idLinha`, `horario`),
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`) ON DELETE CASCADE
);

CREATE TABLE `linhaPontos` (
  `idLinha` integer,
  `codPonto` integer,
  PRIMARY KEY (`idLinha`, `codPonto`),
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`) ON DELETE CASCADE,
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
  FOREIGN KEY (`idLinha`) REFERENCES `linha` (`codLinha`) ON DELETE CASCADE,
  FOREIGN KEY (`cobrador`) REFERENCES `cobrador` (`matricula`)
);

CREATE TABLE `passagem` (
  `id` integer PRIMARY KEY,
  `numCartao` integer NOT NULL,
  `valor` float NOT NULL,
  `dataHora` datetime,
  `idViagem` integer NOT NULL,
  FOREIGN KEY (`numCartao`) REFERENCES `cartaoTransporte` (`id`),
  FOREIGN KEY (`idViagem`) REFERENCES `viagem` (`id`) ON DELETE CASCADE
);

CREATE TABLE historico_linha (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codLinha INT NOT NULL,
    valor_antigo FLOAT NOT NULL,
    valor_atual FLOAT NOT NULL,
    FOREIGN KEY (codLinha) REFERENCES linha(codLinha) ON DELETE CASCADE
);


-- Trigger para atualizar histórico
DELIMITER $$
CREATE TRIGGER trg_linha_valor_update
BEFORE UPDATE ON linha
FOR EACH ROW
BEGIN
    IF OLD.valor <> NEW.valor THEN
        INSERT INTO historico_linha (codLinha, valor_antigo, valor_atual)
        VALUES (OLD.codLinha, OLD.valor, NEW.valor);
    END IF;
END $$
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE registrar_passagem(
    IN p_id INT,
    IN p_numCartao INT,
    IN p_idViagem INT,
    IN p_dataHora DATETIME
)
BEGIN
    DECLARE v_saldo FLOAT;
    DECLARE v_valorLinha FLOAT;

    -- Busca o saldo atual do cartão
    SELECT saldo INTO v_saldo
    FROM cartaoTransporte
    WHERE id = p_numCartao;

    -- Verifica se o cartão existe
    IF v_saldo IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cartão inexistente.';
    END IF;

    -- Busca o valor da linha da viagem
    SELECT l.valor INTO v_valorLinha
    FROM viagem v
    JOIN linha l ON v.idLinha = l.codLinha
    WHERE v.id = p_idViagem;

    -- Verifica se tem saldo suficiente
    IF v_saldo < v_valorLinha THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Saldo insuficiente para realizar a passagem.';
    END IF;

    -- Insere a passagem usando o ID e a data fornecidos pelo usuário
    INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem)
    VALUES (
        p_id,
        p_numCartao,
        v_valorLinha,
        p_dataHora,
        p_idViagem
    );

    -- Atualiza o saldo do cartão
    UPDATE cartaoTransporte
    SET saldo = saldo - v_valorLinha
    WHERE id = p_numCartao;

END $$

DELIMITER ;


CREATE VIEW viagem_envolvidos AS
SELECT 
    v.id AS idViagem,
    v.data,
    v.horaSaida,
    v.horaChegada,

    m.nome AS nomeMotorista,
    c.nome AS nomeCobrador,
    o.placa AS onibusPlaca,
    l.nome AS nomeLinha,

    COUNT(pa.id) AS quantidadePassageiros,

    GROUP_CONCAT(pas.nome SEPARATOR ', ') AS nomesPassageiros

FROM viagem v
LEFT JOIN motorista m ON v.motorista = m.CNH
LEFT JOIN cobrador c ON v.cobrador = c.matricula
LEFT JOIN onibus o ON v.placa = o.placa
LEFT JOIN linha l ON v.idLinha = l.codLinha
LEFT JOIN passagem pa ON pa.idViagem = v.id
LEFT JOIN cartaoTransporte ct ON pa.numCartao = ct.id
LEFT JOIN passageiro pas ON ct.Usuario = pas.CPF

GROUP BY 
    v.id, v.data, v.horaSaida, v.horaChegada,
    m.nome, c.nome, o.placa, l.nome;
