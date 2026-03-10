using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("What is your grade percentage? ");
        string userInput = Console.ReadLine();
        int percentage = int.Parse(userInput);

        string letter;

        if (percentage >= 90) letter = "A";
        else if (percentage >= 80) letter = "B";
        else if (percentage >= 70) letter = "C";
        else if (percentage >= 60) letter = "D";
        else letter = "F";

        string sign = "";
        int lastDigit = percentage % 10;
        if (letter != "A" && letter != "F")
        {
            if (lastDigit >= 7) sign = "+";
            else if (lastDigit < 3) sign = "-";
        }

        Console.WriteLine($"Your letter grade is {letter}{sign}.");
        if (percentage >= 70) Console.WriteLine("Congratulations! You passed the course.");
        else Console.WriteLine("Keep trying! You can do better next time.");
    }
}
