
            # EventConnect: A Full-Stack Event Management Platform

            ## Time to complete: 48h

            ## Scenario
            A local community organization called 'CommunityBridge' is looking to modernize how they manage and promote their events. They currently use spreadsheets and social media posts, which has become inefficient as they've grown. They've approached your company to build a full-stack event management platform called 'EventConnect'.

EventConnect needs to allow organizers to create, manage, and track events while providing community members with a user-friendly interface to discover, register for, and provide feedback on events. The platform should support various event types (workshops, seminars, volunteer opportunities, fundraisers) and provide analytics on attendance and engagement.

The organization needs both an admin portal for event organizers and a public-facing website for community members. They want a modern, responsive design that works well on mobile devices, as many community members primarily use smartphones.

You've been tasked with developing a proof-of-concept for this platform that demonstrates the core functionality. The solution should use FastAPI for the backend API, React for the frontend, and a SQL database for data storage. Additionally, the system should be designed to eventually integrate with AWS services for scalability and reliability.

            ## Outcomes
            ['Implement a FastAPI backend with endpoints for CRUD operations on events, users, and registrations', 'Create a React frontend with responsive design for both admin and public-facing interfaces', 'Design and implement a SQL database schema with proper relationships between entities', 'Implement user authentication and role-based authorization (admin/organizer vs. regular user)', 'Create a dashboard for admins to view analytics on event attendance and engagement', 'Implement a search and filter functionality for events based on date, category, and keywords', 'Set up proper data validation and error handling throughout the application', 'Implement a rating and feedback system for events', 'Create a notification system for upcoming events (email notifications can be simulated)', 'Document the API using OpenAPI/Swagger', 'Implement proper serialization/deserialization of data between frontend and backend', 'Create a proof-of-concept integration with AWS API Gateway (can use mock endpoints if needed)']

            ## Constraints
            ['The backend must be implemented using FastAPI with proper routing and dependency injection', 'The frontend must be built with React and should use hooks for state management', 'Database interactions must use SQLAlchemy ORM with proper transaction handling', 'The application must include proper authentication using JWT tokens', 'All API endpoints must include appropriate input validation using Pydantic models', 'The code must include error handling with appropriate HTTP status codes and error messages', 'The frontend must be responsive and work on both desktop and mobile devices', 'The application must include at least 5 unit tests for critical backend functionality', 'All sensitive information (passwords, API keys) must be properly secured', 'The code must follow best practices for both Python and JavaScript/React', 'You may use free tier AWS services or mock the AWS integration if needed', 'The solution should be designed with scalability in mind, even if not fully implemented']
            