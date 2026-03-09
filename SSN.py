import re


def validate_phone(phone):
    """Validates phone numbers in format: (123) 456-7890"""
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.fullmatch(pattern, phone))


def validate_ssn(ssn):
    """Validates SSN in format: 123-45-6789"""
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.fullmatch(pattern, ssn))


def validate_zip(zip_code):
    """Validates Zip in format: 12345 or 12345-6789"""
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.fullmatch(pattern, zip_code))


def main():
    print("--- User Input Validation Tool ---")

    # Get Inputs
    user_phone = input("Enter Phone Number ((123) 456-7890): ")
    user_ssn = input("Enter SSN ( 123-45-6789): ")
    user_zip = input("Enter Zip Code (12345): ")

    # Display Results
    print("\n--- Validation Results ---")
    print(f"Phone ({user_phone}): {'VALID' if validate_phone(user_phone) else 'INVALID'}")
    print(f"SSN ({user_ssn}): {'VALID' if validate_ssn(user_ssn) else 'INVALID'}")
    print(f"Zip ({user_zip}): {'VALID' if validate_zip(user_zip) else 'INVALID'}")


if __name__ == "__main__":
    main()