//Sarah Weidlein
//Final Project
//This program is a basic turn based game that requests the player to input either attack or heal options fighting an enemy with the support of their party member 



class TurnBaseCombat
{
    private static void Main(string[] args)
    {
        int playerHP = 40;
        int enemyHP = 20;


        int playerAttack = 5;
        int enemyAttack = 20;

        int healAmount = 5;

        
        Random random = new Random();

        

        while (playerHP > 0 && enemyHP > 0)
        {
            //player turn
            Console.WriteLine("---------------------");
            Console.WriteLine("---------------------");
            Console.WriteLine("-- Player turn --");
            DisplayHP(ref playerHP, enemyHP);

            Console.WriteLine("Enter 'a' to attack or 'h' to heal");

            string choice = Console.ReadLine();

            if (choice == "a")
            {
                enemyHP -= playerAttack;
                Console.WriteLine("Player attack enemy and deals " + playerAttack + " damage");
            }
            else
            {
                playerHP += healAmount;
                Console.WriteLine("Player restores " + healAmount + " heal points");
            }

          
            //enemy turn

            if (enemyHP > 0)
            {
                Console.WriteLine("---------------------");
                Console.WriteLine("---------------------");
                Console.WriteLine("-- Enemy Turn --");

                int enemyChoice = random.Next(0, 2);

                if (enemyChoice == 0)
                {
                    playerHP -= enemyAttack;
                    Console.WriteLine("Enemy attacks and deals " + enemyAttack + " damage");

                    Console.WriteLine("---------------------");
                    Console.WriteLine("---------------------");
                    Console.WriteLine("-- Party Member Turn --");
                    List<int> partyAttack = new List<int> { 2, 1, 0 };

                    int block = random.Next(0, partyAttack.Count);
                    Console.Write(partyAttack[block]);

                    playerHP += partyAttack[block];
                    Console.WriteLine(" Enemy attack blocked, restored " + partyAttack[block] + " points");

                }
                else
                {
                    enemyHP += healAmount;
                    Console.WriteLine("Enemy restores " + healAmount + " heal points");
                }
            }

        }


        if (playerHP > 0)
        {
            Console.WriteLine("Congrats you won! :)");

        }

        else
        {
            Console.WriteLine("You lost :(");
            Restore(playerHP);
        }

    }
    private static void DisplayHP(ref int playerHP, int enemyHP)
    {
        Console.WriteLine("Player HP - " + playerHP + " Enemy HP - " + enemyHP);
        

    }
    private static int Restore(int playerHP)
    {
        if (playerHP == 0)
        {
            return 10;
        }
        return 10;
    }

   
    
}
