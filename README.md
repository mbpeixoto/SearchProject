# Content Management and Distribution Application 🌐

This project is a content management and distribution system designed to handle text, images, and videos efficiently. The application integrates four core components to deliver a seamless experience: a Content API, ElasticSearch, MongoDB, and Amazon S3.

---

## Application Workflow ⚙️

### 1. Content Insertion 🗂️✔️

When an editor publishes new content, the following steps are executed: 

- **Submission**: The content, which can include text, images, and videos, is sent to the Content Publishing API. In this project, to simplify things, we use the populate.py file to perform this function and focus only on the search and content display APIs.
- **Text and Metadata Storage**: Storage of textual content and metadata (e.g., author, publication date, categories) in MongoDB.
- **Media Storage**: Images and videos are uploaded to Amazon S3 for secure and scalable storage.
- **Indexing**: To enable fast searches, the API indexes the content in ElasticSearch. This includes essential fields like title, summary, and categories, making it easy to locate relevant content quickly.

### 2. Content Search and Retrieval 🔍🔄

When a user searches for content through the frontend, the following steps occur:

- **Search Request**: The frontend sends a search query (e.g., "sports content") to the Content Management API.
- **Search Execution**: The API queries ElasticSearch to identify the most relevant content based on the provided criteria, such as keywords, date, or category.
- **Search Results**: ElasticSearch returns a list of results containing content IDs and basic details (e.g., title, summary, media links).
- **Content Selection**: The user selects a specific piece of content from the search results.
- **Detailed Retrieval**: The API fetches the complete textual details from MongoDB and retrieves media URLs from Amazon S3.
- **Response Assembly**: The API combines the text (from MongoDB) and media URLs (from S3) to deliver a complete response back to the frontend.

---

## Key Components 🔑📚

- **Content API**: Manages the publishing and retrieval of content.
- **ElasticSearch**: Powers the search functionality for fast and efficient queries.
- **MongoDB**: Stores textual content and metadata.
- **Amazon S3**: Handles the storage of images and videos.

---

## Benefits 📈✨

- **Scalability**: Designed to handle large volumes of content and user queries.
- **Fast Search**: ElasticSearch enables quick and accurate search results.
- **Secure Storage**: Amazon S3 ensures the safety and accessibility of media files.
- **Centralized Data**: MongoDB provides a reliable repository for text and metadata.

---

## Setup Instructions ⚙️🌐🗂️


1. **Clone the Repository**: 

   ```
   git clone https://github.com/mbpeixoto/SearchProject.git
   ```

2. **Install Dependencies**: 

   - Ensure you have Docker and Docker-Compose installed.
   - Run:
     ```
     docker-compose down --volumes --remove-orphans
     docker-compose up --build
     ```

3. **Populate the Database**: 

   - Access the backend container:
     ```
     docker exec -it backend /bin/bash
     python populate.py
     ```

4. **Access the Frontend**:

   - Open `http://localhost:8501` in your browser.

---

## Future Improvements 🌐📈✨

- **Content Recommendations**: Add machine learning for personalized suggestions.
- **Real-Time Updates**: Integrate WebSocket for instant content updates.
- **Advanced Analytics**: Use tools like Kibana to analyze user behavior.

---


