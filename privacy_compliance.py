import hashlib

def anonymize_data(data):
    """
    Anonymizes sensitive user data by hashing user IDs and other PII.

    Args:
        data (dict): A dictionary containing user data.

    Returns:
        dict: A dictionary with anonymized user data.
    """
    # Hash the user ID
    if 'user_id' in data:
        data['user_id'] = hashlib.sha256(data['user_id'].encode()).hexdigest()

    # Optionally anonymize other fields (e.g., email, phone number)
    if 'email' in data:
        data['email'] = hashlib.sha256(data['email'].encode()).hexdigest()

    if 'phone' in data:
        data['phone'] = hashlib.sha256(data['phone'].encode()).hexdigest()

    return data

def main():
    # Example user data
    user_data = {
        'user_id': '12345',
        'email': 'user@example.com',
        'phone': '123-456-7890',
        'name': 'John Doe'
    }

    print("Original Data:")
    print(user_data)

    anonymized_data = anonymize_data(user_data)

    print("\nAnonymized Data:")
    print(anonymized_data)

if __name__ == '__main__':
    main()