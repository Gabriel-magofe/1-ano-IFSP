//  6) Escreva um programa para ler uma matriz A de duas dimensões com 4 linhas e 3 colunas. Mostre a quantidade de valores pares e impares.
using System;

class Program
{
    static void Main()
    {
        int[,] A = new int[4, 3];
        int p=0, ip=0;

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
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<3; j++)
            {
                if(A[i, j]%2==0)
                {
                    p++;
                }
                else
                {
                    ip++;
                }
            }
            
        } 
        Console.WriteLine($"Quantidade de valores pares: {p}");
        Console.WriteLine($"Quantidade de valores impares: {ip}");
    }
}