# Django Awesome App

Welcome to Django Awesome App! This is a powerful web application built with Django to do amazing things.

## Installation

1. Create a directory and then Clone the repository:
    ```bash
    git clone https://github.com/keishcf/application_portal.git
    ``
   
2. Navigate into the project directory :
    ```bash
    cd application_portal
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Perform database migrations:
    ```bash
    python manage.py migrate
    ```

7. (Optional) Load initial data (fixtures):
    ```bash
    python manage.py loaddata initial_data
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

9. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the app.

## Usage

- To start using Django Awesome App, sign up for an account or log in if you already have one.
- Explore the various features and functionalities of the application.
- If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

- - To start using Django Awesome App, sign up for an account. An email confirmation will be sent to your email address.
- If you want to view the confirmation link for email confirmation in the console, follow these steps:
    1. Check the console you used to runserver You might see something like this:
        ```bash
        Content-Type: text/plain; charset="utf-8"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Subject: [example.com] Please Confirm Your Email Address
        From: webmaster@localhost
        To: test@gmail.com
        Date: Fri, 26 Apr 2024 03:34:58 -0000
        Message-ID: <171410249848.16792.14062758299409197362@keishcf>
        
        Hello from example.com!
        
        You're receiving this email because user test has given your email address to register an account on example.com.
        
        To confirm this is correct, go to http://127.0.0.1:8000/account/confirm-email/Mg:1s0CMU:y2sY1OyUNdYkCT1bs8SccvxsaJERCpXo7zur1x6XmO0/
        
        Thank you for using example.com!
        example.com
        -------------------------------------------------------------------------------
        ```
    2. Then copy and paste the email link sent to activate that looks like this yours might be different though:
        ```python
        To confirm this is correct, go to http://127.0.0.1:8000/account/confirm-email/Mg:1s0CMU:y2sY1OyUNdYkCT1bs8SccvxsaJERCpXo7zur1x6XmO0/
        ```
    3. Paste it through to any browser and click confrim email your will be sent to the login page.
    4. after that login and start using the application.

- Explore the various features and functionalities of the application.
- If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

## Contributing

Contributions are welcome! If you'd like to contribute to Django Awesome App, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the `main` branch of the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
