using System;

public class MainClass
{
    public static void Main()
    {
        // string line = Console.ReadLine(); // ввод числа в десятеричной системе 

        // int x = int.Parse(line);

        int x = 12;

        string answer = Convert.ToString(x, 16);

        //Запишите тут Ваш код

        Console.WriteLine(answer);
    }
}