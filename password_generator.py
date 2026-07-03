import random
import string


class InvalidPasswordError(Exception):
    pass


def generate_password(length=12):
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ''.join(
        random.choices(
            string.ascii_letters +
            string.digits +
            string.punctuation,
            k=length - 4
        )
    )

    password = uppercase + lowercase + digit + special + remaining

    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)


def validate_password(password):

    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must be at least 8 characters long."
        )

    if not any(char.isupper() for char in password):
        raise InvalidPasswordError(
            "Password must contain at least one uppercase letter."
        )

    if not any(char.islower() for char in password):
        raise InvalidPasswordError(
            "Password must contain at least one lowercase letter."
        )

    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError(
            "Password must contain at least one digit."
        )

    if not any(char in string.punctuation for char in password):
        raise InvalidPasswordError(
            "Password must contain at least one special character."
        )

    return True


def main():
    print("===== PASSWORD GENERATOR & VALIDATOR =====")

    generated_password = generate_password()

    print("\nGenerated Password:")
    print(generated_password)

    user_password = input(
        "\nEnter a password to validate: "
    )

    try:
        if validate_password(user_password):
            print("Password is valid and strong!")

    except InvalidPasswordError as e:
        print("Validation Error:", e)


main()