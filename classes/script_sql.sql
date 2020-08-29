create database ExameFinal;

use ExameFinal;

CREATE TABLE Cliente (
	id_cliente integer PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(20) NOT NULL,
	nome VARCHAR(30) NOT NULL,
    telefone int(10),
    endereco varchar(30),
    renda float(10)
);

CREATE TABLE Agendamento(
	id_agendamento integer PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(30),
    data datetime,
    status VARCHAR(20),
    id_cliente integer
);

ALTER TABLE Agendamento ADD CONSTRAINT fk_agendamento FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente);

INSERT INTO `Cliente` (`cpf`, `nome`, `telefone`, `endereco`, `renda`) 
VALUES ('012.236.987-44', 'Leticia', 2132132, 'rua 8 seto 3', 1000.0 ), 
('021.545.258-55', 'Nara', 2132132, 'rua 2 seto 3', 600.0),
('024.547.658-77', 'Hermione', 3451213, 'rua 9 seto 3', 1300.0),
('224.137.258-71', 'Luiza', 65732, 'rua 3 seto 2', 1500.0),
('344.547.452-11', 'Davi', 22231, 'rua 3 seto 6', 3300.0),
('443.432.142-27', 'Sara', 435341, 'rua 1 seto 1', 300.0);

INSERT INTO `Agendamento` (`descricao`,`data`,`status`,`id_cliente`)
VALUES ('massagem completa', '2020-09-20 12:40', 'não foi', 1),
('massagem nos pés', '2020-08-20 09:30', 'foi', 2),
('acupuntura', '2010-02-03 13:30', 'nao', 3),
('massagem nas costas', '2020-06-12 12:35', 'sim', 2),
('massagem completa', '2017-07-14 16:40', 'nao', 4),
('massagem nas pernas', '2016-03-03 09:10', 'nao', 6),
('reabilitação de acidente', '2017-12-23 19:00', 'sim', 2),
('acupuntura', '2016-05-13 11:30', 'sim', 1);