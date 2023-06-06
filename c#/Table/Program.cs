using System;

public class MainClass
{
    public static void Main()
    {
        // Console.WriteLine("Введите два числа через пробел: длина и ширина стола");
        // string line = Console.ReadLine();
        // string[] splitString = line.Split(' ');

        // double length = Convert.ToDouble(splitString[0]); // длина
        // double width = Convert.ToDouble(splitString[1]); // ширина

        double length = 2;
        double width = 3;

        double area = (length - 0.2) * (width - 0.2);

        Console.WriteLine($"Площадь стола: {area}"); 
    }
}