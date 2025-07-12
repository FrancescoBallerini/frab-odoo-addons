{
    "name": "Login Show Custom Message",
    "summary": """
        Show custom message in login and signup by setting
        html fields in website configuration.
    """,
    "version": "14.0.1.0.0",
    "depends": [
        "website",
        "auth_signup",
    ],
    "author": "Francesco Ballerini",
    "website": "https://github.com/FrancescoBallerini",
    "data": [
        "views/auth_signup_login_templates.xml",
        "views/website.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
