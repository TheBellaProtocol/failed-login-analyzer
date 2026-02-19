# analyze_logins.py

def analyze_logins(username, current_day_logins, average_day_logins):
    """
    Analyze user login activity.

    Args:
        username (str): Name of the user.
        current_day_logins (int): Number of logins for the current day.
        average_day_logins (int): Average number of logins per day.

    Returns:
        float: Ratio of current day logins to average logins.
    """
    print(f"Current day login total for {username} is {current_day_logins}")
    print(f"Average logins per day for {username} is {average_day_logins}")
    
    login_ratio = current_day_logins / average_day_logins

    if login_ratio >= 3:
        print("Alert! This account has more login activity than normal.")
    
    return login_ratio


if __name__ == "__main__":
    # Example usage
    login_analysis = analyze_logins("ejones", 9, 3)
    print(f"{login_analysis=}")
