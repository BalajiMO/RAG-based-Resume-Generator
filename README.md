# 💼 RAG Resume Generator

A sophisticated Resume Generator powered by **Retrieval-Augmented Generation (RAG)** that creates personalized resumes based on job descriptions and requirements.

## 🚀 Features

### 🔍 **RAG Technology**
- **Retrieval**: Searches through a comprehensive database of resume content
- **Generation**: Uses AI to create relevant resume sections
- **Personalization**: Tailors content to specific job roles and requirements

### 🎯 **Smart Features**
- **Skill Detection**: Automatically identifies relevant skills from job descriptions
- **Multiple Sections**: Generates professional summary, experience, skills, projects, and education
- **Industry Focus**: Tailors content based on target industry
- **Experience Levels**: Supports entry-level to senior positions
- **Download Ready**: Export generated resumes as text files

### 🎨 **User Interface**
- **Modern UI**: Clean, professional interface with custom styling
- **Sidebar Configuration**: Easy-to-use controls for job role and preferences
- **Real-time Generation**: Instant resume creation with RAG context
- **Visual Feedback**: Skill tags and progress indicators

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🛠️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd rag_resume
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### 1. **Load Resume Data**
First, populate the database with resume content:
```bash
python load_data.py
```

### 2. **Run the Application**
Start the Streamlit application:
```bash
streamlit run app.py
```

### 3. **Generate Resumes**
1. Open your browser and navigate to the application (usually `http://localhost:8501`)
2. Enter your target job role in the sidebar
3. Select your experience level and industry focus
4. Click "Generate Resume" to create your personalized resume
5. Download the generated resume as a text file

## 🎯 How It Works

### **RAG Process**
1. **Query Processing**: Your job description is processed and embedded
2. **Retrieval**: The system searches through resume content database using semantic similarity
3. **Context Building**: Relevant resume content is retrieved and combined
4. **Generation**: AI generates personalized resume sections using the retrieved context
5. **Output**: Complete, tailored resume is generated and displayed

### **Database Content**
The system includes resume content covering:
- **Technical Skills**: Programming languages, frameworks, tools
- **Soft Skills**: Communication, leadership, problem-solving
- **Industry Experience**: Various sectors and roles
- **Project Management**: Agile, tools, methodologies
- **Education & Certifications**: Academic and professional development

## 📁 Project Structure

```
rag_resume/
├── app.py              # Main Streamlit application
├── load_data.py        # Script to populate resume database
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── data/              # ChromaDB data storage
│   ├── chroma.sqlite3
│   └── [chromadb files]
└── venv/              # Virtual environment (if used)
```

## 🎨 Customization

### **Adding More Resume Content**
Edit `load_data.py` to add more resume blocks:
```python
resume_blocks = [
    "Your custom resume content here",
    "More relevant experience descriptions",
    # ... add more content
]
```

### **Modifying Generation Prompts**
In `app.py`, update the `prompts` dictionary in `generate_resume_section()`:
```python
prompts = {
    "summary": "Your custom summary prompt",
    "experience": "Your custom experience prompt",
    # ... modify prompts
}
```

### **Styling Changes**
Modify the CSS in the `st.markdown()` section of `app.py` to customize the appearance.

## 🔧 Technical Details

### **Models Used**
- **Embedding Model**: `all-MiniLM-L6-v2` (Sentence Transformers)
- **Generation Model**: `google/flan-t5-small` (Transformers)
- **Vector Database**: ChromaDB for efficient similarity search

### **Performance**
- **Caching**: Models are cached using `@st.cache_resource`
- **Efficient Retrieval**: ChromaDB provides fast similarity search
- **Responsive UI**: Streamlit ensures smooth user experience

## 💡 Tips for Better Results

1. **Be Specific**: Include key technologies and skills in your job description
2. **Industry Context**: Mention the target industry or company type
3. **Experience Level**: Select the appropriate experience level for better tailoring
4. **Key Skills**: Include relevant technical skills in your job description

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding more resume content to `load_data.py`
- Improving the generation prompts
- Enhancing the UI/UX
- Adding new features

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **ChromaDB** for vector database functionality
- **Sentence Transformers** for embedding capabilities
- **Transformers** for text generation
- **Streamlit** for the web interface

---

**💼 RAG Resume Generator** - Powered by modern AI and RAG technology to create personalized, professional resumes. 
