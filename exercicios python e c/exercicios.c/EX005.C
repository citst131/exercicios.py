/*
    Autor: Jean Lucas Thomazelli Silva
    Data: 14/03/2026
    Objetivo: calcular o tempo para estudar e tempo livre
*/
#include <stdio.h>

int main()
{
    int minutos;
    int tempo_estudo;
    int tempo_disciplina;
    int tempo_descanso;

    minutos = 60 + 40;
    tempo_estudo = 100;
    tempo_disciplina = 100 / 6;
    tempo_descanso = 100 % 6;
    printf("1 hora e 40 minutos e igual a %d minutos!\n", minutos);
    printf("Tempo total de estudos %d minutos!\n", tempo_estudo);
    printf("Tempo para cada materia %d minutos!\n", tempo_disciplina);
    printf("Tempo livre para descanso %d minutos!\n", tempo_descanso);
    return 0;
}
