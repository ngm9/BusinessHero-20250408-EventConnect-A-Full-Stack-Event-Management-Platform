# EventConnect: A Full-Stack Event Management Platform

## Project Overview
EventConnect is a full-stack event management platform for a local community organization called 'CommunityBridge'. The platform allows organizers to create, manage, and track events while providing community members with a user-friendly interface to discover, register for, and provide feedback on events.

## Technical Stack
- Backend: FastAPI (Python)
- Frontend: React
- Database: PostgreSQL (or any SQL database of your choice)
- ORM: SQLAlchemy
- Authentication: JWT
- Cloud Integration: AWS API Gateway

## Project Structure
The project is divided into two main parts:
1. Backend API (`/backend`)
2. Frontend Application (`/frontend`)

## Getting Started

### Backend Setup
1. Create a virtual environment and install dependencies
2. Set up your database and update the connection string in the configuration
3. Run migrations to create the database schema
4. Start the FastAPI server

### Frontend Setup
1. Install dependencies using npm or yarn
2. Configure the API endpoint in the environment variables
3. Start the development server

## Project Requirements

### Core Features
- User authentication and role-based authorization
- Event creation, management, and discovery
- Event registration and attendance tracking
- Feedback and rating system for events
- Admin dashboard with analytics
- Search and filter functionality
- Notification system for upcoming events

### Technical Requirements
- Implement proper data validation using Pydantic models
- Use SQLAlchemy for database interactions
- Implement proper error handling and status codes
- Create a responsive UI that works on mobile devices
- Document the API using OpenAPI/Swagger
- Implement integration with AWS API Gateway
- Write unit tests for critical functionality

## Deliverables
1. Complete source code for both backend and frontend
2. Documentation on how to set up and run the application
3. API documentation
4. A brief explanation of your design decisions and any challenges faced

## Notes
- You can use free tier AWS services or mock the AWS integration if needed
- Focus on demonstrating your skills in FastAPI, React, and SQL database integration
- Prioritize functionality over visual design, but ensure the UI is responsive and user-friendly