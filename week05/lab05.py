def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    valid_ages = []
    for user in users:
        if 'age' in user:
            age = user['age']
            if isinstance(age, (int, float)) and not isinstance(age, bool):
                valid_ages.append(age)
    
    if not valid_ages:
        return 0.0
    
    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    emails = []
    for user in users:
        if user.get('is_active') and 'email' in user:
            emails.append(user['email'])
    
    return emails