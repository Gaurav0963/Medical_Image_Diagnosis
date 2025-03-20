# Medical Imaging Diagnosis Web Application

A web application for medical image analysis using OpenAI's GPT-4 Vision model and Streamlit for the frontend.

## Prerequisites

- Python 3.8 or higher
- Conda (Miniconda or Anaconda)
- OpenAI API key with access to GPT-4 Vision model

## Setup Instructions

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Gaurav0963/Medical_Image_Diagnosis.git

# Navigate to the project directory
cd Medical_Image_Diagnosis
```

### 2. Create and Activate Conda Environment

```bash
# Create a new conda environment named med_img
conda create -n med_img python=3.11 -y

# Activate the environment
conda activate med_img

# Install required packages
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

```
med_img/
├── app.py              # Streamlit frontend
├── main.py            # Flask backend
├── prompts.py         # AI prompts and templates
├── requirements.txt   # Python dependencies
└── .env              # Environment variables
```

## Running the Application

1. Start the Flask backend:
```bash
python main.py
```

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run app.py
```

3. Open your browser and navigate to:
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

## Features

- Medical image analysis using GPT-4 Vision
- Detailed radiological assessment
- Medical literature references
- Semantic search through past analyses
- Secure API key management
- User-friendly interface

## API Endpoints

- `POST /analyze`: Analyze medical images
- `GET /health`: Health check endpoint

## Error Handling

The application includes comprehensive error handling for:
- OpenAI API errors
- Image processing errors
- Request validation errors
- General server errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-4 Vision model
- Streamlit for the frontend framework
- Flask for the backend framework
