---
title: "Worklenz: 高效团队的全方位项目管理工具"
slug: worklenz-project-management-tool
description: |
  Worklenz 是一款全方位的项目管理工具，旨在提升团队效率。它提供任务管理、时间追踪、资源管理等综合解决方案，帮助团队更好地协作与沟通。使用 React 和 TypeScript 开发，支持 Docker 部署。
tags: 
  - projectmanagement
  - dev
  - tool
  - collaboration
  - docker
pubDatetime: 2025-04-22T14:13:28+08:00
ogImage: https://opengraph.githubassets.com/7138393f6c357ace04f67c62b6fec6cb62e47927eca8fcaac2336968d3a042a6/Worklenz/worklenz
---

[原文链接](https://github.com/Worklenz/worklenz)

---

[![Worklenz Logo](https://camo.githubusercontent.com/31ab8d7f62073a474f333cd8328ad90f8716f99df546afcb8b8b39ade0738e9f/68747470733a2f2f6170702e776f726b6c656e7a2e636f6d2f6173736574732f69636f6e732f69636f6e2d313434783134342e706e67)](https://worklenz.com)\
Worklenz
========

[](#------------------------worklenz----)

[Task Management](https://worklenz.com/task-management/) | [Time Tracking](https://worklenz.com/time-tracking/) | [Analytics](https://worklenz.com/analytics/) | [Resource Management](https://worklenz.com/resource-management/) | [Project Templates](https://worklenz.com/templates/)

[![Worklenz](https://camo.githubusercontent.com/4728547ad66513f6cdebbefd9d906bf9f65ee4c521c65f4353578b416d8de960/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f6865726f2d766965772e706e67)](https://worklenz.com)

Worklenz is a project management tool designed to help organizations improve their efficiency. It provides a comprehensive solution for managing projects, tasks, and collaboration within teams.

## Features

[](#features)

* **Project Planning**: Create and organize projects, assign tasks to team members.
* **Task Management**: Break down projects into smaller tasks, set due dates, priorities, and track progress.
* **Collaboration**: Share files, leave comments, and communicate seamlessly with your team members.
* **Time Tracking**: Monitor time spent on tasks and projects for better resource allocation and billing.
* **Reporting**: Generate detailed reports on project status, team workload, and performance metrics.

## Tech Stack

[](#tech-stack)

This repository contains the frontend and backend code for Worklenz.

* **Frontend**: Built using React with Ant Design as the UI library.
* **Backend**: Built using TypeScript, Express.js, with PostgreSQL as the database.

## Requirements

[](#requirements)

* Node.js version v18 or newer
* PostgreSQL version v15 or newer
* Docker and Docker Compose (for containerized setup)

## Getting Started

[](#getting-started)

These instructions will help you set up and run the Worklenz project on your local machine for development and testing purposes.

### Prerequisites

[](#prerequisites)

* Node.js (version 18 or higher)
* PostgreSQL database
* An S3-compatible storage service (like MinIO) or Azure Blob Storage

### Option 1: Manual Installation

[](#option-1-manual-installation)

1. Clone the repository

```
git clone https://github.com/Worklenz/worklenz.git
cd worklenz
```

2. Set up environment variables

   * Copy the example environment files

   ```
   cp .env.example .env
   cp worklenz-backend/.env.example worklenz-backend/.env
   ```

   * Update the environment variables with your configuration

3. Install dependencies

```
# Install backend dependencies
cd worklenz-backend
npm install

# Install frontend dependencies
cd ../worklenz-frontend
npm install
```

4. Set up the database

```
# Create a PostgreSQL database named worklenz_db
cd worklenz-backend

# Execute the SQL setup files in the correct order
psql -U your_username -d worklenz_db -f database/sql/0_extensions.sql
psql -U your_username -d worklenz_db -f database/sql/1_tables.sql
psql -U your_username -d worklenz_db -f database/sql/indexes.sql
psql -U your_username -d worklenz_db -f database/sql/4_functions.sql
psql -U your_username -d worklenz_db -f database/sql/triggers.sql
psql -U your_username -d worklenz_db -f database/sql/3_views.sql
psql -U your_username -d worklenz_db -f database/sql/2_dml.sql
psql -U your_username -d worklenz_db -f database/sql/5_database_user.sql
```

5. Start the development servers

```
# In one terminal, start the backend
cd worklenz-backend
npm run dev

# In another terminal, start the frontend
cd worklenz-frontend
npm run dev
```

6. Access the application at <http://localhost:5000>

### Option 2: Docker Setup

[](#option-2-docker-setup)

The project includes a fully configured Docker setup with:

* Frontend React application
* Backend server
* PostgreSQL database
* MinIO for S3-compatible storage

1. Clone the repository:

```
git clone https://github.com/Worklenz/worklenz.git
cd worklenz
```

2. Start the Docker containers (choose one option):

**Using Docker Compose directly**

```
docker-compose up -d
```

3. The application will be available at:

   * Frontend: <http://localhost:5000>
   * Backend API: <http://localhost:3000>
   * MinIO Console: <http://localhost:9001> (login with minioadmin/minioadmin)

4. To stop the services:

```
docker-compose down
```

## Configuration

[](#configuration)

### Environment Variables

[](#environment-variables)

Worklenz requires several environment variables to be configured for proper operation. These include:

* Database credentials
* Session secrets
* Storage configuration (S3 or Azure)
* Authentication settings

Please refer to the `.env.example` files for a full list of required variables.

### MinIO Integration

[](#minio-integration)

The project uses MinIO as an S3-compatible object storage service, which provides an open-source alternative to AWS S3 for development and production.

* **MinIO Console**: <http://localhost:9001>

  * Username: minioadmin
  * Password: minioadmin

* **Default Bucket**: worklenz-bucket (created automatically when the containers start)

### Security Considerations

[](#security-considerations)

For production deployments:

1. Use strong, unique passwords and keys for all services
2. Do not commit `.env` files to version control
3. Use a production-grade PostgreSQL setup with proper backup procedures
4. Enable HTTPS for all public endpoints
5. Review and update dependencies regularly

## Contributing

[](#contributing)

We welcome contributions from the community! If you'd like to contribute, please follow our [contributing guidelines](https://github.com/Worklenz/worklenz/blob/main/CONTRIBUTING.md).

## Security

[](#security)

If you believe you have found a security vulnerability in Worklenz, we encourage you to responsibly disclose this and not open a public issue. We will investigate all legitimate reports.

Email <info@worklenz.com> to disclose any security vulnerabilities.

## License

[](#license)

This project is licensed under the [MIT License](https://github.com/Worklenz/worklenz/blob/main/LICENSE).

## Screenshots

[](#screenshots)

[![Worklenz task views](https://camo.githubusercontent.com/2af57502b17ea4fcb5252097c8c1a22b3fd2eec53d0b604ee2c65259da721f98/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f7461736b2d76696577732d766965772e706e67)](https://worklenz.com/features/task-management/)

[![Worklenz time tracking](https://camo.githubusercontent.com/1220cd6c1998624dc39faf1db44257378ee0812bcec6ab05d34670a8e11d9c4d/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f74696d652d747261636b696e672d766965772e706e67)](https://worklenz.com/features/time-tracking/)

[![Worklenz analytics](https://camo.githubusercontent.com/8f13b4fa78eb87ea24ed3856daade2c0e77327526951096d191bd8f5372129a7/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f616e616c79746963732d766965772e706e67)](https://worklenz.com/features/analytics/)

[![Worklenz scheduler](https://camo.githubusercontent.com/19c8659f1e6dad9de2dfe832037fe1c460aaef2e158e8eca3ef79a152a4d72e9/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f7363686564756c652d766965772e706e67)](https://worklenz.com/features/resource-management/)

[![Worklenz templates](https://camo.githubusercontent.com/e93bf574e178d81bef1a14fdc50359554534189f162201ba2fa59b957107fbfb/68747470733a2f2f776f726b6c656e7a2e73332e616d617a6f6e6177732e636f6d2f6173736574732f73637265656e73686f74732f74656d706c617465732d766965772e706e67)](https://worklenz.com/features/templates/)

### Contributing

[](#contributing-1)

We welcome contributions from the community! If you'd like to contribute, please follow our [contributing guidelines](https://github.com/Worklenz/worklenz/blob/main/CONTRIBUTING.md).

### License

[](#license-1)

Worklenz is open source and released under the [GNU Affero General Public License Version 3 (AGPLv3)](https://github.com/Worklenz/worklenz/blob/main/LICENSE).

By contributing to Worklenz, you agree that your contributions will be licensed under its AGPL.

# Worklenz React

[](#worklenz-react)

This repository contains the React version of Worklenz with a Docker setup for easy development and deployment.

## Getting Started with Docker

[](#getting-started-with-docker)

The project includes a fully configured Docker setup with:

* Frontend React application
* Backend server
* PostgreSQL database
* MinIO for S3-compatible storage

### Prerequisites

[](#prerequisites-1)

* Docker and Docker Compose installed on your system
* Git

### Quick Start

[](#quick-start)

1. Clone the repository:

```
git clone https://github.com/Worklenz/worklenz.git
cd worklenz
```

2. Start the Docker containers (choose one option):

**Option 1: Using the provided scripts (easiest)**

* On Windows:

  ```
  start.bat
  ```

* On Linux/macOS:

  ```
  ./start.sh
  ```

**Option 2: Using Docker Compose directly**

```
docker-compose up -d
```

3. The application will be available at:

   * Frontend: <http://localhost:5000>
   * Backend API: <http://localhost:3000>
   * MinIO Console: <http://localhost:9001> (login with minioadmin/minioadmin)

4. To stop the services (choose one option):

**Option 1: Using the provided scripts**

* On Windows:

  ```
  stop.bat
  ```

* On Linux/macOS:

  ```
  ./stop.sh
  ```

**Option 2: Using Docker Compose directly**

```
docker-compose down
```

## MinIO Integration

[](#minio-integration-1)

The project uses MinIO as an S3-compatible object storage service, which provides an open-source alternative to AWS S3 for development and production.

### Working with MinIO

[](#working-with-minio)

MinIO provides an S3-compatible API, so any code that works with S3 will work with MinIO by simply changing the endpoint URL. The backend has been configured to use MinIO by default, with no additional configuration required.

* **MinIO Console**: <http://localhost:9001>

  * Username: minioadmin
  * Password: minioadmin

* **Default Bucket**: worklenz-bucket (created automatically when the containers start)

### Backend Storage Configuration

[](#backend-storage-configuration)

The backend is pre-configured to use MinIO with the following settings:

```
// S3 credentials with MinIO defaults
export const REGION = process.env.AWS_REGION || "us-east-1";
export const BUCKET = process.env.AWS_BUCKET || "worklenz-bucket";
export const S3_URL = process.env.S3_URL || "http://minio:9000/worklenz-bucket";
export const S3_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID || "minioadmin";
export const S3_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY || "minioadmin";
```

The S3 client is initialized with special MinIO configuration:

```
const s3Client = new S3Client({
  region: REGION,
  credentials: {
    accessKeyId: S3_ACCESS_KEY_ID || "",
    secretAccessKey: S3_SECRET_ACCESS_KEY || "",
  },
  endpoint: getEndpointFromUrl(), // Extracts endpoint from S3_URL
  forcePathStyle: true, // Required for MinIO
});
```

### Environment Configuration

[](#environment-configuration)

The `.env` file includes the necessary configuration for using MinIO:

```
STORAGE_PROVIDER=s3
AWS_REGION=us-east-1
AWS_BUCKET=worklenz-bucket
S3_ACCESS_KEY_ID=minioadmin
S3_SECRET_ACCESS_KEY=minioadmin
S3_URL=http://minio:9000
```

When the backend service starts, it will use these environment variables to connect to MinIO for file storage.

## Development

[](#development)

For development, you can use the provided Docker setup which includes all necessary dependencies. The code will be running inside containers, but you can still edit files locally and see changes reflected in real-time.

## Production Deployment

[](#production-deployment)

For production deployment:

1. Update the `.env` file with production settings
2. Build custom Docker images or use the provided ones
3. Deploy using Docker Compose or a container orchestration platform like Kubernetes

For MinIO in production, consider:

* Setting up proper credentials (change default minioadmin/minioadmin)
* Configuring persistent storage
* Setting up proper networking and access controls
* Using multiple MinIO instances for high availability


