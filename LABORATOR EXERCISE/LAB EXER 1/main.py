
active_tickets = []

while True:
    print("\n=========================================")
    print(" IT Automation Incident Ticket Manager ")
    print("=========================================")
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for a specific incident ticket")
    print("4. Remove a resolved incident ticket")
    print("5. Display total number of active tickets")
    print("6. Exit")
    print("=========================================")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        inc_id = input("Enter Incident ID: ")
        bot = input("Enter Bot Name: ")
        desc = input("Enter Short Description: ")
        
        ticket = {"id": inc_id, "bot": bot, "description": desc}
        active_tickets.append(ticket)
        print("Ticket added successfully!")

    elif choice == '2':
        if len(active_tickets) == 0:
            print("No active tickets right now.")
        else:
            print("\n--- Active Tickets ---")
            for i in range(len(active_tickets)):
                t = active_tickets[i]
                print(f"Ticket {i+1} | ID: {t['id']} | Bot: {t['bot']} | Desc: {t['description']}")

    elif choice == '3':
        search_id = input("Enter Incident ID to search: ")
        found = False
        for t in active_tickets:
            if t["id"] == search_id:
                print("\nTicket Found!")
                print("Incident ID:", t["id"])
                print("Bot:", t["bot"])
                print("Description:", t["description"])
                found = True
                break
        
        if found == False:
            print("Ticket not found.")

    elif choice == '4':
        remove_id = input("Enter Incident ID to remove: ")
        found = False
        for i in range(len(active_tickets)):
            if active_tickets[i]["id"] == remove_id:
                active_tickets.pop(i)
                print("Ticket removed successfully!")
                found = True
                break
        
        if found == False:
            print("Ticket not found. Cannot remove.")

    elif choice == '5':
        print("Total active tickets:", len(active_tickets))

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
