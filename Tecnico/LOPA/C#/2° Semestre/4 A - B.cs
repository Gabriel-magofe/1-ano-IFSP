// 4) Ler duas matrizes A e B, cada uma de duas dimensões com quatro linhas e três colunas. Construir uma matriz C de mesma dimensão, a qual é formada pela subtração dos elementos da matriz A com os elementos da matriz B. Apresentar a matriz C.
using System;

class Program
{
    static void Main()
    {
        int[,] A = new int[4, 3];
        int[,] B = new int[4, 3];
        int[,] C = new int[4, 3];

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                A[i, j] = Random.Shared.Next(1, 10);
                B[i, j] = Random.Shared.Next(1, 10);
                C[i, j] = A[i, j] - B[i, j];
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

        Console.WriteLine("\nMatriz B:");
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(B[i, j] + "\t");
            }
            Console.WriteLine();
        }

        Console.WriteLine("\nMatriz C:");
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(C[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }
}