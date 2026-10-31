
# Student Email and Identifier Validation

import re


def validate_email(email):
    errors = []

    # Check @ separator
    if email.count("@") == 0:
        errors.append("Missing @ separator")
        return errors

    if email.count("@") > 1:
        errors.append("Multiple @ separators")
        return errors

    username, domain = email.split("@")

    # Check missing components
    if username == "":
        errors.append("Missing username")

    if domain == "":
        errors.append("Missing domain")
        return errors

    # Validate username
    if username:
        if username.startswith(".") or username.endswith("."):
            errors.append("Username cannot start or end with a dot")

        if ".." in username:
            errors.append("Consecutive dots in username")

        if not re.fullmatch(r"[A-Za-z0-9_.]+", username):
            errors.append("Invalid characters in username")

    # Check domain separator
    if "." not in domain:
        errors.append("Missing domain extension")
        return errors

    parts = domain.split(".")

    if any(part == "" for part in parts):
        errors.append("Malformed domain separators")

    # Validate domain labels
    for part in parts[:-1]:
        if part:
            if not re.fullmatch(r"[A-Za-z0-9-]+", part):
                errors.append("Invalid characters in domain")

            if part.startswith("-") or part.endswith("-"):
                errors.append("Domain label cannot start or end with hyphen")

    # Validate domain extension
    extension = parts[-1]

    if extension == "":
        errors.append("Missing domain extension")
    elif not re.fullmatch(r"[A-Za-z]+", extension):
        errors.append("Invalid characters in domain extension")
    elif len(extension) < 2:
        errors.append("Domain extension must have at least 2 letters")

    return errors


def validate_id(reg_id):
    errors = []

    # Required format: CSE-2026-001
    if reg_id == "":
        errors.append("Missing registration ID")
        return errors

    parts = reg_id.split("-")

    if len(parts) != 3:
        errors.append("Incorrect number of ID components")
        return errors

    department, year, number = parts

    if department == "":
        errors.append("Missing department code")
    elif department != "CSE":
        errors.append("Invalid department code")

    if year == "":
        errors.append("Missing admission year")
    elif not re.fullmatch(r"\d{4}", year):
        errors.append("Year must contain exactly 4 digits")

    if number == "":
        errors.append("Missing student number")
    elif not re.fullmatch(r"\d{3}", number):
        errors.append("Student number must contain exactly 3 digits")

    return errors


# Main program
email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

email_errors = validate_email(email)
id_errors = validate_id(reg_id)

print("\n--- VALIDATION RESULTS ---")

if len(email_errors) == 0:
    print("Email: VALID")
else:
    print("Email: INVALID")
    for error in email_errors:
        print("-", error)

if len(id_errors) == 0:
    print("Registration ID: VALID")
else:
    print("Registration ID: INVALID")
    for error in id_errors:
        print("-", error)

print("\nValidation completed.")

