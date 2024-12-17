# DevHelper CLI

**DevHelper CLI** is a command-line tool designed to automate repetitive tasks during the setup and development of projects. It helps developers quickly generate common files like `.gitignore`, `README.md`, `LICENSE`, `.env`, and Docker-related templates.

---

## **Features**

- **Generate `.gitignore` files** for specific programming languages (Python, Node.js, Java).
- **Create a `README.md` file** with project title and description.
- **Generate standard license files** (MIT, Apache 2.0).
- **Create an `.env` file** with placeholders for environment variables.
- **Generate a `Dockerfile`** for Python or Node.js projects.
- **Generate a `docker-compose.yml` file** to set up services.

---

## **Installation**

Follow these steps to install DevHelper CLI locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DevHelper-CLI.git
   cd DevHelper-CLI
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install DevHelper CLI as a local package:
   ```bash
   pip install -e .
   ```

---

## **Usage**

You can now use DevHelper CLI directly with the command `devhelper`.

### 1. Initialize the CLI
```bash
devhelper init
```
Output:
```
Initializing DevHelper CLI!
```

### 2. Generate a `.gitignore` File
```bash
devhelper generate-gitignore python
```
Output:
```
.gitignore file generated for 'python'.
```

### 3. Generate a `README.md`
```bash
devhelper generate-readme "My Project" "This is a sample project description"
```
Output:
```
README.md file generated with title: 'My Project'.
```

### 4. Generate a License
```bash
devhelper generate-license MIT
```
Output:
```
LICENSE file generated with license: 'MIT'.
```

### 5. Generate an `.env` File
```bash
devhelper generate-env
```
Output:
```
.env file generated with basic placeholders.
```

### 6. Generate a `docker-compose.yml`
```bash
devhelper generate-compose python
```
Output:
```
docker-compose.yml generated for 'python'.
```

---

## **Testing**

Run the automated tests to ensure everything works correctly:

```bash
pytest tests/
```

---

## **Contributing**

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch and open a pull request.

---

## **License**

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## **Contact**

If you have any questions or suggestions, feel free to open an issue or reach out to the author via email at `your.email@example.com`.

