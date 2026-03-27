/*
ALUNO: JEAN LUCAS THOMAZELLI SILVA
DATA: 21/03/2026
OBJETIVO: Calcular salario de cada funcionario e lucro liquido da loja
*/

#include <stdio.h>

int main()
{
    int funcionarios;
    int bicicletas_vendidas;
    float salario_minimo;
    float custo_bicicleta;
    float bicicleta_acrescimo;
    float salario_funcionario;
    float faturamento;
    float custo_total;
    float comissao;
    float comissao_funcionario;
    float pagar_funcionario;
    float lucro_loja;

    printf("Quantos funcionarios tem na loja?\n");
    scanf("%d", &funcionarios);

    printf("Qual o valor do salario minimo?\n");
    scanf("%f", &salario_minimo);

    printf("Qual o custo de cada bicicleta?\n");
    scanf("%f", &custo_bicicleta);

    printf("Quantas bicicletas foram vendidas?\n");
    scanf("%d", &bicicletas_vendidas);

    bicicleta_acrescimo = custo_bicicleta + (custo_bicicleta * 0.5);
    comissao = custo_bicicleta * 0.15;
    comissao_funcionario = comissao * bicicletas_vendidas / funcionarios;
    salario_funcionario = salario_minimo * 2 + comissao_funcionario;
    faturamento = bicicleta_acrescimo * bicicletas_vendidas;
    custo_total = custo_bicicleta * bicicletas_vendidas;
    pagar_funcionario = salario_funcionario * funcionarios;
    lucro_loja = faturamento - custo_total - pagar_funcionario;

    printf("O salario final de cada funcionario e de R$ %.2f!\n", salario_funcionario);
    printf("O lucro da loja e de R$ %.2f!\n", lucro_loja);

    return 0;
}
