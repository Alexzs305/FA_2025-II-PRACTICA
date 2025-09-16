using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA3_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {

        }
        static void ejer1() 
        {
            //DECLARAMOS VARIABLES
            string nombre, carrera;

            //MOSTRAR MENSAJE
            Console.Write("Ingrese su nombnre:");
            nombre = Console.ReadLine();

            Console.Write("Ingrese su carrera:");
            carrera = Console.ReadLine();

            //MOSTRAR RESULTADO
            Console.WriteLine($"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}");

        }
        static void ejer2()
        {
            Console.WriteLine("Ingrese un numero x: ");
            int x = int.Parse(Console.ReadLine());

            Console.WriteLine("Ingrese un numero y: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double reesultado = (double)x / (double)y;

            Console.WriteLine("suma: "+(x+y));
            Console.WriteLine("resta: "+(x-y));
            Console.WriteLine("multiplicacion: "+(x*y));
            Console.WriteLine("division: "+(x/y));
        }
        static void ejer3()
        {
            Console.WriteLine("\"ALEXIS\"");
        }
        static void ejer4()
        {
            Console.WriteLine("Ingrese un numero decimal: ");
            double num = Convert.ToDouble(Console.ReadLine());

            double raiz2= Math.Sqrt(num);
            int redo = (int)Math.Round(num);
            double cubo = Math.Pow(num, 3);
            double raiz3 = Math.Pow(num, 1 / 3d);

            Console.WriteLine("Raiz2" + raiz2);
            Console.WriteLine("Redondeo: " + redo);
            Console.WriteLine("Cubo: " + cubo); 
            Console.WriteLine("Raiz3: " + raiz3);
        }
        static void ejer5()
        {
            Console.Write("Ingrese un numnero: ");
            string num = Console.ReadLine();

            int entero = int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("Resto: "+(entero%2));
            Console.WriteLine("Division" + (deci / 3));

        }
        static void ejer6()
        {

        }
        static void ejer7() 
        {
            
        }
    }
}
