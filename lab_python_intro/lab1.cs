using System;

class Program
{
    static double GetCoef(int index, string prompt)
    {
        double coef;
        Console.Write(prompt);
        try
        {
            coef = double.Parse(Environment.GetCommandLineArgs()[index]);
        }
        catch
        {
            while (!double.TryParse(Console.ReadLine(), out coef))
            {
                Console.WriteLine("Not a valid value");
                Console.Write(prompt);
            }
        }
        return coef;
    }

    static void GetSquareRoots(double root, ref double[] result)
    {
        if (root >= 0)
        {
            root = Math.Sqrt(root);
            if (root > 0)
            {
                Array.Resize(ref result, result.Length + 1);
                result[result.Length - 1] = -root;
            }
            Array.Resize(ref result, result.Length + 1);
            result[result.Length - 1] = root;
        }
    }

    static double[] GetRoots(double a, double b, double c)
    {
        double[] result = new double[0];
        double d = b * b - 4 * a * c;
        Console.WriteLine("Discriminant = " + d);
        if (d == 0.0)
        {
            double root = -b / (2.0 * a);
            GetSquareRoots(root, ref result);
        }
        else if (d > 0.0)
        {
            double sqd = Math.Sqrt(d);
            double root1 = (-b + sqd) / (2.0 * a);
            double root2 = (-b - sqd) / (2.0 * a);
            GetSquareRoots(root1, ref result);
            GetSquareRoots(root2, ref result);
        }
        return result;
    }

    static void Main()
    {
        double a = GetCoef(1, "Enter real A:");
        double b = GetCoef(2, "Enter real B:");
        double c = GetCoef(3, "Enter real C:");
        Console.WriteLine($"You entered: {a}x^4 + {b}x^2 + {c} = 0");
        double[] roots = GetRoots(a, b, c);
        int lenRoots = roots.Length;
        if (lenRoots == 0)
        {
            Console.WriteLine("There are no real roots");
        }
        else if (lenRoots == 1)
        {
            Console.WriteLine($"There is one real root:\n{roots[0]}");
        }
        else
        {
            Console.WriteLine($"There are {lenRoots} real roots:");
            Array.ForEach(roots, root => Console.WriteLine(root));
        }
    }
}
