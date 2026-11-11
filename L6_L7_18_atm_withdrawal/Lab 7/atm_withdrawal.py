def notes_needed(amount):
    """Calculates the number of 100 notes needed for a given amount safely."""
    if not isinstance(amount, str):
        return 0
    
    # Strip spaces and commas
    cleaned = amount.replace(',', '').strip()
    
    # Check if string represents a non-negative integer
    if not cleaned.isdigit():
        return 0
        
    val = int(cleaned)
    return val // 100

def mask_card(card_number):
    """Masks a card number safely, showing only the last 4 digits."""
    if not isinstance(card_number, str):
        return "XXXX XXXX XXXX XXXX"
    
    groups = card_number.split()
    
    # Standard format: 4 groups of digits
    if len(groups) >= 4:
        return "XXXX XXXX XXXX " + groups[3]
    
    # Fallback for alternative space-separated or raw string formats
    digits = "".join(card_number.split())
    if len(digits) >= 4:
        return "XXXX XXXX XXXX " + digits[-4:]
        
    return "XXXX XXXX XXXX XXXX"

def average_withdrawal(amounts_csv):
    """Calculates integer average of CSV withdrawal amounts safely."""
    if not isinstance(amounts_csv, str):
        return 0
        
    amounts = []
    for a in amounts_csv.split(','):
        cleaned = a.strip()
        # Accept positive and negative integer strings
        if cleaned.lstrip('-').isdigit() and cleaned != '':
            amounts.append(int(cleaned))
            
    # Guard against empty lists to avoid ZeroDivisionError
    if not amounts:
        return 0
        
    return sum(amounts) // len(amounts)

def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result)

if __name__ == "__main__":
    main()