//   . 5) Construa um algoritmo que, para uma matriz 4 x 3, calcule a soma dos elementos de cada uma das linhas e escreva as somas obtidas. O algoritmo deve mostrar também o número da linha que apresentou a maior soma.

int[,] A = new int[4, 3];
int[] soma = new int[4];

for (int i = 0; i < 4; i++)
{
    for (int j = 0; j < 3; j++)
    {
        A[i, j] = Random.Shared.Next(1, 10);
    }
}
Console.WriteLine("Matriz A:");
for (int i = 0; i < 4; i++)
{
    for (int j = 0; j < 3; j++)
    {
        Console.Write(A[i, j] + "\t");
    }
    Console.WriteLine();
}
for (int i = 0; i < 4; i++)
{
    soma[i] = A[i, 0] + A[i, 1] + A[i, 2];
}

int linhaMaior = 0;
int somaMaior = 0;
for (int i = 0; i < 4; i++)
{
    if (soma[i] > somaMaior)
    {
        somaMaior = soma[i];
        linhaMaior = i + 1;
    }
}

if (somaMaior == 0)
{
    Console.WriteLine("A matriz não possui linhas com soma maior.");
}
else
{
    Console.WriteLine($"A linha com maior soma é a linha {linhaMaior} e a soma é {somaMaior}.");
}
