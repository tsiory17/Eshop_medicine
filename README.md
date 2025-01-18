# Eshop Medicine

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies](#technologies)
6. [Contributing](#contributing)
7. [License](#license)

## Description
Eshop Medicine is an online platform designed to simplify the process of purchasing medications. Users can browse a wide range of pharmaceutical products, add them to their cart, and securely check out—all from the comfort of their home.

## Features
- **User Authentication**: Secure login and registration for users.
- **Product Browsing**: Easy navigation and search functionality to find medications.
- **Shopping Cart**: Add, remove, and update items in the cart.
- **Order Management**: Track orders and view order history.
- **Secure Payment**: Multiple payment options with a secure checkout process.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/eshop-medicine.git
    ```
2. Navigate to the project directory:
    ```bash
    cd eshop-medicine
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
- **Home Page**: Browse featured products and categories.
- **Product Page**: View detailed information about a medication.
- **Cart Page**: Review items in your cart and proceed to checkout.
- **Profile Page**: Manage your account information and order history.

## Technologies
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Authentication**: Django Allauth
- **Payment Gateway**: Stripe

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License.
