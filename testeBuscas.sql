-- ==== EMPRESA ====
INSERT INTO empresa (CNPJ, telefone, nome, endereco) VALUES
('11111111000101', '1122334455', 'TransSul Transportes', 'Av. Central, 100'),
('22222222000102', '2233445566', 'CidadeBus', 'Rua das Flores, 45'),
('33333333000103', '3344556677', 'Viação Norte', 'Av. Paulista, 1500'),
('44444444000104', '4455667788', 'Metropolitan', 'Rua Verde, 200'),
('55555555000105', '5566778899', 'EcoBus', 'Av. Azul, 320');


-- ==== PONTO DE ÔNIBUS ====
INSERT INTO pontoOnibus (codPonto, endereco) VALUES
(1, 'Rua das Palmeiras, 10'),
(2, 'Av. Brasil, 500'),
(3, 'Praça Central'),
(4, 'Rua Nova, 1200'),
(5, 'Terminal Rodoviário');


-- ==== LINHA ====
INSERT INTO linha (codLinha, idEmpresa, nome, valor) VALUES
(101, '11111111000101', 'Linha Sul', 4.50),
(102, '11111111000101', 'Linha Leste', 5.50),
(201, '22222222000102', 'Linha Centro', 6.50),
(301, '33333333000103', 'Linha Norte', 7.50),
(401, '44444444000104', 'Linha Oeste', 8.50);



-- ==== HORÁRIOS DAS LINHAS ====
INSERT INTO horariosLinha (idLinha, horario) VALUES
(101, '06:00:00'),
(101, '12:00:00'),
(102, '08:30:00'),
(201, '07:00:00'),
(301, '09:00:00');


-- ==== LINHA-PONTOS ====
INSERT INTO linhaPontos (idLinha, codPonto) VALUES
(101, 1),
(101, 2),
(102, 3),
(201, 4),
(301, 5);


-- ==== MOTORISTA ====
INSERT INTO motorista (CNH, nome, telefone, jornada) VALUES
('M1111', 'João Santos', '11987654321', 8),
('M2222', 'Carlos Pereira', '11987654322', 6),
('M3333', 'Rafael Souza', '11987654323', 8),
('M4444', 'Pedro Lima', '11987654324', 10),
('M5555', 'Lucas Rocha', '11987654325', 8);


-- ==== COBRADOR ====
INSERT INTO cobrador (matricula, nome, telefone, escala) VALUES
('C111', 'Maria Silva', '11976543210', 1),
('C222', 'Fernanda Alves', '11976543211', 2),
('C333', 'José Gomes', '11976543212', 1),
('C444', 'Paulo Oliveira', '11976543213', 2),
('C555', 'André Ramos', '11976543214', 3);


-- ==== ÔNIBUS ====
INSERT INTO onibus (placa, capacidade, idEmpresa) VALUES
('AAA1A11', 45, '11111111000101'),
('BBB2B22', 50, '11111111000101'),
('CCC3C33', 40, '22222222000102'),
('DDD4D44', 60, '33333333000103'),
('EEE5E55', 55, '44444444000104');


-- ==== PASSAGEIRO ====
INSERT INTO passageiro (CPF, nome, telefone, email, dataNascimento) VALUES
('11111111111', 'Ana Costa', '11911111111', 'ana@example.com', '1990-01-01'),
('22222222222', 'Bruno Melo', '11922222222', 'bruno@example.com', '1985-05-10'),
('33333333333', 'Clara Souza', '11933333333', 'clara@example.com', '1998-12-12'),
('44444444444', 'Diego Nunes', '11944444444', 'diego@example.com', '1992-06-15'),
('55555555555', 'Elisa Torres', '11955555555', 'elisa@example.com', '2000-09-09');


-- ==== CARTÃO DE TRANSPORTE ====
INSERT INTO cartaoTransporte (id, Usuario, saldo) VALUES
(1, '11111111111', 45.50),
(2, '22222222222', 30.00),
(3, '33333333333', 12.75),
(4, '44444444444', 100.00),
(5, '55555555555', 5.00);


-- ==== VIAGEM ====
INSERT INTO viagem (id, motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data) VALUES
(1, 'M1111', 'C111', 'AAA1A11', 101, '07:30:00', '06:00:00', '2025-10-19'),
(2, 'M2222', 'C222', 'BBB2B22', 102, '09:00:00', '08:30:00', '2025-10-19'),
(3, 'M3333', 'C333', 'CCC3C33', 201, '08:00:00', '07:00:00', '2025-10-19'),
(4, 'M4444', null, 'DDD4D44', 301, '10:00:00', '09:00:00', '2025-10-19'),
(5, 'M5555', 'C555', 'EEE5E55', 401, '12:00:00', '11:00:00', '2025-10-19');


-- ==== PASSAGEM ====
INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem) VALUES
(1, 1, 4.50, '2025-10-19 06:05:00', 1),
(2, 2, 4.50, '2025-10-19 08:40:00', 2),
(3, 3, 4.50, '2025-10-19 07:10:00', 3),
(4, 4, 4.50, '2025-10-19 09:10:00', 4),
(5, 5, 4.50, '2025-10-19 11:05:00', 5);

-- ==== VIAGEM MTS PASSAGEIROS ====
INSERT INTO viagem (id, motorista, cobrador, placa, idLinha, horaChegada, horaSaida, data) VALUES
(6, 'M1111', 'C111', 'AAA1A11', 101, '18:00:00', '17:00:00', '2025-10-20');

INSERT INTO passageiro (CPF, nome, telefone, email, dataNascimento) VALUES
('66666666666', 'Paulo Mendes', '11966666666', 'paulo@example.com', '1993-03-12'),
('77777777777', 'Rita Soares', '11977777777', 'rita@example.com', '1995-07-29'),
('88888888888', 'Gustavo Araujo', '11988888888', 'gustavo@example.com', '1999-02-18'),
('99999999999', 'Helena Freitas', '11999999999', 'helena@example.com', '2001-04-22'),
('10101010101', 'Daniel Lima', '11910101010', 'daniel@example.com', '1990-08-08'),
('12121212121', 'Marina Castro', '11912121212', 'marina@example.com', '1994-01-15'),
('13131313131', 'Thiago Ramos', '11913131313', 'thiago@example.com', '1992-12-10'),
('14141414141', 'Larissa Dias', '11914141414', 'larissa@example.com', '1997-06-30'),
('15151515151', 'Felipe Braga', '11915151515', 'felipe@example.com', '1996-09-09'),
('16161616161', 'Isabela Campos', '11916161616', 'isabela@example.com', '1998-11-11'),
('17171717171', 'Otávio Ribeiro', '11917171717', 'otavio@example.com', '1993-02-02'),
('18181818181', 'Camila Moura', '11918181818', 'camila@example.com', '1999-07-07'),
('19191919191', 'Marcelo Vieira', '11919191919', 'marcelo@example.com', '1991-05-05'),
('20202020202', 'Patricia Alves', '11920202020', 'patricia@example.com', '2000-10-10'),
('21212121212', 'Brenda Lopes', '11921212121', 'brenda@example.com', '1997-03-03');

INSERT INTO cartaoTransporte (id, Usuario, saldo) VALUES
(6, '66666666666', 50),
(7, '77777777777', 50),
(8, '88888888888', 50),
(9, '99999999999', 50),
(10, '10101010101', 50),
(11, '12121212121', 50),
(12, '13131313131', 50),
(13, '14141414141', 50),
(14, '15151515151', 50),
(15, '16161616161', 50),
(16, '17171717171', 50),
(17, '18181818181', 50),
(18, '19191919191', 50),
(19, '20202020202', 50),
(20, '21212121212', 50);

INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem) VALUES
(6, 6, 4.50, '2025-10-20 17:02:00', 6),
(7, 7, 4.50, '2025-10-20 17:03:00', 6),
(8, 8, 4.50, '2025-10-20 17:04:00', 6),
(9, 9, 4.50, '2025-10-20 17:05:00', 6),
(10, 10, 4.50, '2025-10-20 17:06:00', 6),
(11, 11, 4.50, '2025-10-20 17:07:00', 6),
(12, 12, 4.50, '2025-10-20 17:08:00', 6),
(13, 13, 4.50, '2025-10-20 17:09:00', 6),
(14, 14, 4.50, '2025-10-20 17:10:00', 6),
(15, 15, 4.50, '2025-10-20 17:11:00', 6),
(16, 16, 4.50, '2025-10-20 17:12:00', 6),
(17, 17, 4.50, '2025-10-20 17:13:00', 6),
(18, 18, 4.50, '2025-10-20 17:14:00', 6),
(19, 19, 4.50, '2025-10-20 17:15:00', 6),
(20, 20, 4.50, '2025-10-20 17:16:00', 6);
