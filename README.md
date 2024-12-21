# SQL Query Chatbot with Google Gemini API

## Overview
This project is a SQL Query Chatbot that integrates with the Google Gemini API, allowing users to connect to a MySQL server and execute SQL queries using natural language input. By employing prompt engineering, the chatbot effectively interprets user queries and transforms them into SQL statements. This tool aims to make database querying more accessible to users without SQL expertise.

## Features
- **Prompt Engineering**: Accurately processes English input to generate SQL queries.
- **Google Gemini API Integration**: Provides robust query parsing and conversion capabilities.
- **MySQL Connectivity**: Supports seamless integration with MySQL for real-time database interaction.
- **User-Friendly Interface**: Simple chat-based setup to enhance user experience.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Technologies Used
- **Python**: Core logic and API interaction.
- **Google Gemini API**: For processing input and generating SQL queries.
- **MySQL-Python (mysql-connector-python)**: Facilitates MySQL database connection.
- **Flask**: Optional for developing a web-based user interface.

## Installation
1. **Clone the Repository**: Clone the project repository to your local environment.
2. **Set Up Python Environment**: Create and activate a Python virtual environment.
3. **Install Dependencies**: Ensure all required Python packages are installed.
4. **Configure MySQL**: Set up and configure access to your MySQL database.
5. **Google Gemini API Key**: Obtain an API key and include it in your environment variables.

## Configuration
- Create a configuration file or use environment variables for sensitive data such as database credentials and API keys.
- Ensure database connection settings (host, user, password, database) are properly configured.
- Use `.env` or similar methods for secure storage of configuration details.

## Usage
1. **Start the Application**: Run the chatbot locally or host it on a server.
2. **Interact with the Chatbot**: Use the chat interface to type questions or requests in English.
3. **Query Examples**:
   - **User Input**: "List all customers who placed an order in the last month."
   - **Generated SQL**: `SELECT * FROM customers WHERE order_date >= NOW() - INTERVAL 1 MONTH;`

## License
This project is distributed under the MIT License. Refer to the `LICENSE` file for more information.

## Contributing
Contributions are welcome! If you have suggestions or want to enhance the project, please submit an issue or a pull request. For major changes, open an issue to discuss your proposal first.

---

### Contact
For questions, feedback, or support, please reach out via email at your gomesadhikari@gmail.com or submit an issue on the project repository.

---

**Empowering seamless database queries through plain English!**
