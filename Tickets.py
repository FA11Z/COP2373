def validate_purchase(requested, remaining):
    """Function 1: Validates if the purchase meets all constraints."""
    if requested < 1 or requested > 4:
        print("Invalid amount. You can only buy between 1 and 4 tickets.")
        return False
    if requested > remaining:
        print(f"Sorry, we only have {remaining} tickets left.")
        return False
    return True


def run_ticket_sale():
    """Function 2: Manages the sales loop, inputs, and accumulators."""
    total_tickets = 20  # Total inventory
    total_buyers = 0  # Accumulator for total buyers

    print("Welcome to the Cinema Ticket Pre-Sale!")

    # Loop: Continues until all 20 tickets are sold
    while total_tickets > 0:
        try:
            # Input: Prompting user for ticket count
            print(f"\nTickets currently available: {total_tickets}")
            buy_count = int(input("How many tickets would you like to purchase? "))

            # If Statement: Utilizing the validation function
            if validate_purchase(buy_count, total_tickets):
                total_tickets -= buy_count  # Decrement inventory
                total_buyers += 1  # Increment buyer accumulator
                print(f"Purchase confirmed! {total_tickets} tickets remaining.")

        except ValueError:
            print("Please enter a valid numeric integer.")

    # Output: Final display once loop finishes
    print("\n" + "*" * 30)
    print("Pre-sale complete! All tickets sold.")
    print(f"Total number of buyers: {total_buyers}")
    print("*" * 30)


# Entry point
if __name__ == "__main__":
    run_ticket_sale()