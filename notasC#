// Este arquivo serve de notas para os projetos de Game Design do ensino médio da univali

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Preencha abaixo as informações da sua primeira média");
        float AVAparcial1, AVAfinal1, AC1, desempenho1, participacao1, caderno1, autoavaliacao1, produtividade1, AVAp01, AVAf01, AC01, Prod01, M1;
        Console.WriteLine ("Nota da AVA parcial: ");
        AVAparcial1 = float.Parse(Console.ReadLine());
        Console.WriteLine ("Nota da AVA final: ");
        AVAfinal1 = float.Parse(Console.ReadLine());
        Console.WriteLine ("Nota da AC: ");
        AC1 = float.Parse(Console.ReadLine());
        
        Console.WriteLine("Agora as informações da sua produtividade: ");
        
        Console.WriteLine("Nota do desempenho: ");
        desempenho1 = float.Parse(Console.ReadLine());
        Console.WriteLine("Nota da participação: ");
        participacao1 = float.Parse(Console.ReadLine());
        Console.WriteLine("Nota do caderno: ");
        caderno1 = float.Parse(Console.ReadLine());
        Console.WriteLine("Autoavaliação: ");
        autoavaliacao1 = float.Parse(Console.ReadLine());
        
        produtividade1 = (desempenho1 * 0.25f) + (participacao1 * 0.25f) + (caderno1 * 0.25f) + (autoavaliacao1 * 0.25f);
        
        AVAp01 = AVAparcial1 * 0.25f;
        AVAf01 = AVAfinal1 * 0.25f;
        AC01 = AC1 * 0.3f;
        Prod01 = produtividade1 * 0.2f;
        
        M1 = AVAp01 + AVAf01 + AC01 + Prod01;

        Console.WriteLine("Sua média é: " + M1);
    }
}