<h1 align="center">💻 User Management System (CRUD)| FastAPI</h1>
<p>
This project demonstrates the development of a <b>REST API</b> using <b>FastAPI</b> and <b>MySQL Server 8.0</b> to perform complete <b>Create, Read, Update, and Delete (CRUD)</b> operations on user records. The API leverages <b>Pydantic</b> for request validation and was tested using <b>Postman</b> to verify endpoint functionality and ensure seamless interaction with the MySQL database.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
  <li>Create new user records.</li>
  <li>Retrieve all users from the database.</li>
  <li>Fetch a user by ID.</li>
  <li>Update existing user information.</li>
  <li>Delete user records.</li>
  <li>Request validation using Pydantic models.</li>
  <li>RESTful API endpoints tested using Postman.</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<ul>
  <li><b>Python</b></li>
  <li><b>FastAPI</b></li>
  <li><b>MySQL Server 8.0</b></li>
  <li><b>Pydantic</b></li>
  <li><b>MySQL Connector/PyMysql</b></li>
  <li><b>Postman</b></li>
</ul>

<hr>

<h2>📌 API Endpoints</h2>

<table>
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/</td>
    <td>Home Endpoint</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/users/</td>
    <td>Create User</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/users/</td>
    <td>Retrieve All Users</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/users/{user_id}</td>
    <td>Retrieve User by ID</td>
  </tr>
  <tr>
    <td>PUT</td>
    <td>/users/{user_id}</td>
    <td>Update User</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>/users/{user_id}</td>
    <td>Delete User</td>
  </tr>
</table>

<hr>

<h2>🧪 Testing</h2>

<p>
All REST API endpoints were tested using <b>Postman</b> to verify request handling, database connectivity, and CRUD functionality.
</p>

<hr>

<h2>🌍 Real-World Use Case</h2>

<p>
This project serves as the backend for applications that require user data management. It provides RESTful endpoints to create, retrieve, update, and delete user records stored in a MySQL database. Such functionality is commonly used in employee management systems, student portals, customer management applications, healthcare systems, and other platforms that require efficient record management.
</p>

<hr>

<h2>📈 Future Enhancements</h2>

<p>
This project is intentionally implemented as a simple CRUD API for learning and demonstration purposes. It can be further enhanced to support production-level scalability and performance by incorporating:
</p>

<ul>
  <li>MySQL Connection Pooling</li>
  <li>In-Memory Caching (Redis or Local Cache)</li>
  <li>Centralized Logging</li>
  <li>Exception Handling & Custom Error Responses</li>
  <li>Authentication & Authorization (JWT/OAuth2)</li>
  <li>SQLAlchemy ORM Integration</li>
  <li>Dependency Injection</li>
  <li>Docker Containerization</li>
  <li>Unit & Integration Testing</li>
  <li>CI/CD Pipeline Integration</li>
</ul>

<hr>

<h2>📚 Learning Outcome</h2>

<p>
This project demonstrates the implementation of RESTful API development using FastAPI, MySQL integration, SQL-based CRUD operations, request validation with Pydantic, and API testing with Postman while providing a solid foundation for building scalable backend applications.
</p>
