<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Consumo Médio de Gasolina</title>
</head>
<body>
    <h1>Calculadora de Consumo Médio de Gasolina</h1>
    <form method="POST" action="">
        <label for="nome">Nome do Condutor:</label>
        <input type="text" id="nome" name="nome" required><br><br>
        
        <label for="distancia">Distância Percorrida (em km):</label>
        <input type="number" id="distancia" name="distancia" required><br><br>
        
        <label for="combustivel">Combustível Gasto (em litros):</label>
        <input type="number" id="combustivel" name="combustivel" required><br><br>
        
        <input type="submit" value="Calcular">
    </form>
    
    <?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Receber os dados do formulário
        $nome = $_POST['nome'];
        $distancia = $_POST['distancia'];
        $combustivel = $_POST['combustivel'];

        if ($distancia > 0 && $combustivel > 0) {
            // Calcular o consumo médio (em km/l)
            $consumo_medio = $distancia / $combustivel;

            echo "<h2>Olá, $nome! Seu consumo médio foi de " . number_format($consumo_medio, 2, '.', '') . " km/l.</h2>";
            
        
            if ($consumo_medio <= 8) {
                echo "<p>Classificação: Alto Consumo</p>";
            } elseif ($consumo_medio > 8 && $consumo_medio <= 14) {
                echo "<p>Classificação: Consumo Moderado</p>";
            } else {
                echo "<p>Classificação: Bom Consumo</p>";
            }
        } else {
            echo "<p>Por favor, insira valores válidos para distância e combustível.</p>";
        }
    }
    ?>
</body>
</html>