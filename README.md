## Features
- Fetch real-time weather data for any city using the OpenWeatherMap API.
- Display temperature, humidity, and weather description in a clean and responsive UI.
- Modular architecture with separate frontend and backend components.
- CI/CD pipeline using GitHub Actions for automated testing and deployment.

---

## Technologies Used
- **Frontend**:
  - Vue.js (with Vuetify 3 for UI components)
  - TypeScript for type safety
  - Axios for API communication
- **Backend**:
  - FastAPI for building the RESTful API
  - Python-dotenv for environment variable management
  - Requests library for interacting with OpenWeatherMap API
- **DevOps**:
  - GitHub Actions for CI/CD
  - Pytest for backend testing
- **External APIs**:
  - OpenWeatherMap API for weather data
 
## Run
```
cd backend
uvicorn main:app --reload
```

```
cd frontend
npm run dev
```
