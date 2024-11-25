CREATE DATABASE AluguelCarros;

USE AluguelCarros;

CREATE TABLE Veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL
);

-- Inserir veículos de exemplo
INSERT INTO Veiculos (modelo, quantidade) VALUES
('SUV', 2),
('Sedan', 3),
('Hatch', 1);
