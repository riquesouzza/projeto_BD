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
INSERT INTO linha (codLinha, idEmpresa, nome) VALUES
(101, '11111111000101', 'Linha Sul'),
(102, '11111111000101', 'Linha Leste'),
(201, '22222222000102', 'Linha Centro'),
(301, '33333333000103', 'Linha Norte'),
(401, '44444444000104', 'Linha Oeste');


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
(4, 'M4444', NULL,     'DDD4D44', 301, '10:00:00', '09:00:00', '2025-10-19'), -- 🔸 CARDINALIDADE 0 (sem cobrador)
(5, 'M5555', 'C555', 'EEE5E55', 401, '12:00:00', '11:00:00', '2025-10-19');


-- ==== PASSAGEM ====
INSERT INTO passagem (id, numCartao, valor, dataHora, idViagem) VALUES
(1, 1, 4.50, '2025-10-19 06:05:00', 1),
(2, 2, 4.50, '2025-10-19 08:40:00', 2),
(3, 3, 4.50, '2025-10-19 07:10:00', 3),
(4, 4, 4.50, '2025-10-19 09:10:00', 4),
(5, 5, 4.50, '2025-10-19 11:05:00', 5);