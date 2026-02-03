# Project 3 – IAM using Keycloak

## Overview
This project demonstrates Identity and Access Management (IAM) using Keycloak.
A Flask application is integrated to implement Single Sign-On (SSO) using
OpenID Connect (OIDC) and JWT tokens.

---

## Tech Stack
- Keycloak
- Docker
- Python (Flask)
- OpenID Connect (OIDC)
- JWT

---

## Implementation Proof

### Prerequisites
Docker and Python installation verified.

![Docker and Python](screenshots/1.docker_and_python.png)

---

### Keycloak Running
Keycloak server running in Docker.

![Keycloak](screenshots/2.keycloak.png)

---

### Admin Login
Accessed Keycloak Admin Console.

![Admin Login](screenshots/3.admin_signin.png)

---

### Realm Creation
Created custom realm named `infotact`.

![Realm](screenshots/4.infotact_master.png)

---

### Roles Configuration
Created realm roles.

![Roles](screenshots/5.realm_roles.png)

---

### User Creation
Created user `alice`.

![User Alice](screenshots/6.user_alice.png)

---

### Role Mapping
Assigned `developer` role to user `alice`.

![Role Mapping](screenshots/7.role_mapping.png)

---

### Flask Application
Flask application running locally.

![Flask App](screenshots/8.flask_app.png)

---

### Redirect to Keycloak
Application redirecting to Keycloak for authentication.

![Redirect](screenshots/9.redirect_url.png)

---

### JWT Token
Successful authentication returns JWT token.

![JWT](screenshots/result-JWT.png)

---

## Outcome
- Implemented IAM using Keycloak
- Enabled SSO with OpenID Connect
- Verified role-based access using JWT

