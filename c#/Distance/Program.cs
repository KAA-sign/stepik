using System;

public class MainClass
{
    public static void Main()
    {        
        int n = 1500; // преобразуем введенную строку в число 
                                                     // и присваиваем его значение переменной

        int distance = 1000 - (n % 1000); //Запишите тут Ваш код для вычислений

        Console.WriteLine(distance); 
    }
}
