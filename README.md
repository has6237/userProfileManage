# userProfileManage
User profile management system by Python


# User Profile Management System - main.py

## Overview

`main.py` is the main entry point for a command-line User Profile Management System built in Python. It provides a comprehensive authentication and user profile management interface with features for user signup, login, and profile customization.

## Features

### Authentication
- **Signup**: Create new user accounts with name, unique username, and password confirmation
- **Login**: Authenticate existing users with username and password validation

### User Profile Management
- **View Profile**: Display current user's profile information (name, username, password)
- **Change Name**: Update your profile name
- **Change Username**: Modify your username with uniqueness validation
- **Change Password**: Update your account password with confirmation
- **Logout**: Securely log out of your account

## How to Use

### Starting the Program
```bash
python main.py
```

### Main Menu Options
1. **Login** - Sign in with existing credentials
2. **Signup** - Create a new account

### User Menu (After Login)
1. **Logout** - Exit your account
2. **Profile** - View your profile details
3. **Change Name** - Update your name
4. **Change Username** - Modify your username
5. **Change Password** - Change your password

## Data Structure

Users are stored in a list with the following structure:
```python
{
    "name": "User's Full Name",
    "username": "unique_username",
    "password": "user_password"
}
```

## Key Functions

| Function | Purpose |
|----------|---------|
| `menu()` | Display main menu and handle user input |
| `signup()` | Register new users with validation |
| `login()` | Authenticate users and manage login state |
| `usermenu()` | Display options for logged-in users |
| `logout()` | Clear user session and return to main menu |
| `profile()` | Display current user's profile information |
| `changeName()` | Update user's name |
| `changeUsername()` | Update user's username with availability check |
| `changePassword()` | Update user's password with confirmation |

## Notes

- Usernames must be unique across the system
- Passwords require confirmation during signup and password changes
- The system uses in-memory storage (data is lost when the program exits)
- After changing username or password, users must log in again with new credentials
- Invalid menu inputs will prompt the user to try again

## Requirements

- Python 3.x
- No external dependencies required

