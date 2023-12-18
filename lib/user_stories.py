#!/usr/bin/env python3
import click
from models import session, Baristas, Clients

@click.command()
def user_input():
   click.echo("Welcome to Barister- Meal Finder's Landing Page")
   click.echo("There are two key sections. Which do you wish to visit")
   click.echo("A: Move to Barista user stories")
   click.echo("B: Move to Client user stories")
   option = click.prompt("", type = str)

   if option == 'A':
         click.echoA
         ("Welcome to the Barista's  Activity Landing Page")
         click.echo("Choose your Barista activity from the options below:")
         click.echo("1: Add Barista")
         click.echo("2: See All Baristas at your disposal")
         click.echo("3: Find Barista using first name")
         click.echo("4: Find Barista using Barista id")
         click.echo("5: Find Baristas serving your desired meal")
         click.echo("6: Edit Barista's information")
         click.echo("7; Delete Barista from BMF Database")
         click.echo("8: Exit Barista's Activities ")

         sub_option = click.prompt("Enter the Barista Activity Of Your Choice", type=int)
         if sub_option == 1:
            barista_id = click.prompt("Provide Barista's id", type=int)
            first_name = click.prompt("Provide  Barista's First name", type=str)
            last_name = click.prompt("Provide Barista's Last name", type=str)
            meal_served = click.prompt("Provide meals you deal in", type=str)
            age = click.prompt("Provide  Barista's age", type=int)

            click.echo(f" {barista_id} {first_name} {last_name} {meal_served} {age}")
            new_barista = Baristas (barista_id = barista_id, first_name=first_name, last_name=last_name, meal_served=meal_served,age=age)

            session.add(new_barista)
            session.commit()
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()
            

          
           
                        

         elif sub_option == 2:
            result = session.query(Baristas).all()
            click.echo(f"Our Team entails :     {[result]}")

            click.echo("Thank you for viewing our team. Do you wish to go back to Barista's landing page?")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()
                      
         elif sub_option == 3:
            first_name = click.prompt("Enter first_name", type=str)
            barista = session.query(Baristas).filter_by(first_name = first_name).all()
            click.echo (f"Result is {barista}") 
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()





         elif sub_option == 4:
             barista_id = click.prompt("Enter the relevant id", type = int)
             barista = session.query(Baristas).filter_by(barista_id=barista_id).all()
             click.echo(f"The {barista_id} belongs to {barista}")
             click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
             click.echo("1: Go back to landing page")
             click.echo("2: Exit")
             option =click.prompt("Input your response", type =int)
             if option == 1:
               return user_input()

   
         elif sub_option == 5:
            meal_served = click.prompt(" Enter your desired meal to find a barista", type=str)
            barista = session.query(Baristas).filter_by(meal_served=meal_served).all()
            click.echo(f" {barista} makes the most sumptuous meal orders.")
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()
            

         elif sub_option == 6:
            barista_id = click.prompt("Enter the Barista ID you want to edit", type=int)
            barista = session.query(Baristas).filter_by(barista_id=barista_id).first()
            if barista:
               new_meal_served = click.prompt("Enter the new meal served", type=str)
               barista.meal_served = new_meal_served
            session.commit()
            click.echo(f"{barista} meal-served information updated successfully.")
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()

            


         elif sub_option == 7:
            barista_id = click.prompt("Enter the Barista ID you want to delete", type=int)
            barista = session.query(Baristas).filter_by(barista_id=barista_id).first()
            if barista:
               session.delete(barista)
               session.commit()
               click.echo("Barista deleted successfully.")
               click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
               click.echo("1: Go back to landing page")
               click.echo("2: Exit")
               option =click.prompt("Input your response", type =int)
               if option == 1:
                  return user_input()
               else:
                  click.echo("No match for Barista's id entered!!")
         else:
            click.echo("Invalid Output")

   else:
      click.echo("Welcome to the Client's  Activity Landing Page")
      click.echo("Choose your Client-based activity from the options below:")
      click.echo("1: Add Client")
      click.echo("2: See All Clients at your disposal")
      click.echo("3: Find Client using first name")
      click.echo("4: Find Client using Client id")
      click.echo("5: Find Client serving your desired meal")
      click.echo("6: Edit Client's Activities ")
      click.echo("7: Delete Client's information from BMF Database")
      click.echo("8; Exit Client's Activities Client from BMF Database")
    

      sub_option = click.prompt("Enter the Client Activity Of Your Choice", type=int)
      if sub_option == 1:
         client_id = click.prompt("Provide Client's id", type=int)
         first_name = click.prompt("Provide  Client's First name", type=str)
         last_name = click.prompt("Provide Clients's Last name", type=str)
         meal_served = click.prompt("Provide meal order", type=str)
         rank = click.prompt("Please rank our services", type=int)

         click.echo(f" {client_id} {first_name} {last_name} {meal_served} {rank}")
         new_client = Clients (client_id = client_id, first_name=first_name, last_name=last_name, meal_served=meal_served,rank=rank)
         
         session.add(new_client)
         session.commit()
         click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below")
         click.echo("1: Go back to landing page")
         click.echo("2: Exit")
         option =click.prompt("Input your response", type =int)
         if option == 1:
            return user_input()
                  
          

      elif sub_option == 2:
         result = session.query(Clients).all()
         click.echo(f"Our valuable customers entail :     {[result]}")

         click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below")
         click.echo("1: Go back to landing page")
         click.echo("2: Exit")
         option =click.prompt("Input your response", type =int)
         if option == 1:
            return user_input()
                  
      elif sub_option == 3:
         first_name = click.prompt("Enter first_name", type=str)
         client = session.query(Clients).filter_by(first_name = first_name).all()
         click.echo (f"Result is {client}") 
         click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
         click.echo("1: Go back to landing page")
         click.echo("2: Exit")
         option =click.prompt("Input your response", type =int)
         if option == 1:
            return user_input()





      elif sub_option == 4:
         client_id = click.prompt("Enter the relevant id", type = int)
         client = session.query(Clients).filter_by(client_id=client_id).all()
         click.echo(f"The Client id {client_id} belongs to {client}")
         click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
         click.echo("1: Go back to landing page")
         click.echo("2: Exit")
         option =click.prompt("Input your response", type =int)
         if option == 1:
            return user_input()


      elif sub_option == 5:
        meal_served = click.prompt(" Enter your desired meal to find a fellow client with your duolicate meal", type=str)
        client = session.query(Clients).filter_by(meal_served=meal_served).all()
        click.echo(f" {client} enjoys your meal order. Contact him as part of BMF Family")
        click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
        click.echo("1: Go back to landing page")
        click.echo("2: Exit")
        option =click.prompt("Input your response", type =int)
        if option == 1:
           return user_input()

      elif sub_option == 6:
        client_id = click.prompt("Enter the client ID you want to edit", type=int)
        client = session.query(Clients).filter_by(client_id=client_id).first()
        if client:
            new_meal_served = click.prompt("Enter the new meal served", type=str)
            client.meal_served = new_meal_served
            session.commit()
            click.echo("Client information updated successfully.")
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()
        else:
            click.echo("Client not found.")
            click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
            click.echo("1: Go back to landing page")
            click.echo("2: Exit")
            option =click.prompt("Input your response", type =int)
            if option == 1:
               return user_input()
               
      elif sub_option == 7:
            client_id = click.prompt("Enter the client ID you want to delete", type=int)
            client = session.query(Clients).filter_by(client_id=client_id).first()
            if client:
                session.delete(client)
                session.commit()
                click.echo("Client deleted successfully.")
                click.echo("Thank you for choosing Barister-Meal Finder. To move from here select below:")
                click.echo("1: Go back to landing page")
                click.echo("2: Exit")
                option =click.prompt("Input your response", type =int)
                if option == 1:
                   return user_input()
            else:
                click.echo("Client not found.")




if __name__ == '__main__':
    user_input()
    show_all_barista()
    return_barista_main()
    show_bar_by_firstname()


