# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

A web application that helps students track their study sessions, manage their time effectively, and analyze their study habits.

## User stories

Link to User Stories: https://github.com/software-students-spring2025/2-web-app-duodice/issues

## Steps necessary to run the software

1.  **Setup Database:**
    * Install and setup [MongoDB](https://www.mongodb.com/) ([Server/Atlas](https://www.mongodb.com/products/platform/atlas-database) + [Client/Shell](https://www.mongodb.com/try/download/shell)).
    * Create a `.env` file in the project's root directory.
    * Add your MongoDB Connection String and the target cluster name as variables in the `.env` file. This will be used by the application to connect to your database.
        ```dotenv
        # Example .env file content
        MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database_name>?retryWrites=true&w=majority
        CLUSTER_NAME=<your_cluster_name>
        ```

2.  **Setup Python Environment (Recommended):**
    * It's recommended to use a virtual environment to manage dependencies.
    * Create a virtual environment (e.g., named `env`):
        ```bash
        python -m venv env
        ```
    * Activate the virtual environment:
        * On macOS/Linux:
            ```bash
            source env/bin/activate
            ```
        * On Windows:
            ```bash
            .\env\Scripts\activate
            ```

3.  **Install Dependencies:**
    * Ensure all necessary packages listed in `requirements.txt` are installed within your activated virtual environment.
    * Run the following command:
        ```bash
        pip install -r requirements.txt
        ```
    * *(**Note:** The `requirements.txt` file itself should list packages and specific versions, like `pymongo[srv]==3.11.0` or `certifi==2023.7.22`, not pip commands).*

4.  **Run the Application:**
    * Execute the main application file:
        ```bash
        python app.py
        ```

5.  **Access the Application:**
    * Open your web browser and navigate to: `http://127.0.0.1:5000`
    * You can create a new user account or log in to an existing one.
    * To view an account with pre-populated data, use the credentials: username `exampleuser`, password `password` (please minimize edits to this shared test account).

## Task boards

-   [Sprint 1](https://github.com/orgs/software-students-spring2025/projects/6)
-   [Sprint 2](https://github.com/orgs/software-students-spring2025/projects/17)
