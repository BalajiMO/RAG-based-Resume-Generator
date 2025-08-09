from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

resume_blocks = [
    # Technical Skills - Programming
    "Skilled in Python, Flask, and REST APIs. Developed scalable backend services.",
    "Proficient in JavaScript, React, and Node.js for full-stack development.",
    "Experienced in Java, Spring Boot, and microservices architecture.",
    "Strong knowledge of C++, data structures, and algorithms.",
    "Familiar with TypeScript, Angular, and modern frontend frameworks.",
    
    # Data Science & ML
    "Experienced in data analysis using Pandas, NumPy, and Excel.",
    "Built ML models for regression, classification, and clustering tasks.",
    "Experience using Hugging Face Transformers and NLP techniques.",
    "Skilled in TensorFlow and PyTorch for deep learning applications.",
    "Proficient in data visualization with Matplotlib, Seaborn, and Plotly.",
    "Experience with scikit-learn for machine learning pipelines.",
    
    # Cloud & DevOps
    "Familiarity with cloud platforms like AWS and GCP.",
    "Experience with Docker containerization and Kubernetes orchestration.",
    "Proficient in CI/CD pipelines using Jenkins and GitHub Actions.",
    "Knowledge of infrastructure as code using Terraform and CloudFormation.",
    
    # Database & Backend
    "Experience with SQL databases including PostgreSQL and MySQL.",
    "Familiar with NoSQL databases like MongoDB and Redis.",
    "Built RESTful APIs and GraphQL services.",
    "Experience with message queues like RabbitMQ and Apache Kafka.",
    
    # Frontend & UI/UX
    "Designed responsive UIs using React and integrated with backend APIs.",
    "Experience with CSS frameworks like Bootstrap and Tailwind CSS.",
    "Skilled in creating accessible and user-friendly interfaces.",
    "Proficient in modern JavaScript (ES6+) and async programming.",
    
    # Soft Skills
    "Strong communication and team collaboration skills.",
    "Experience leading cross-functional teams and mentoring junior developers.",
    "Excellent problem-solving abilities and analytical thinking.",
    "Proven track record of delivering projects on time and within budget.",
    "Strong presentation skills and ability to explain technical concepts to non-technical stakeholders.",
    
    # Project Management
    "Experience with Agile methodologies including Scrum and Kanban.",
    "Proficient in project management tools like Jira and Asana.",
    "Track record of managing multiple projects simultaneously.",
    "Experience with stakeholder management and requirement gathering.",
    
    # Version Control & Tools
    "Proficient in version control using Git and collaborative tools like GitHub.",
    "Experience with code review processes and maintaining code quality.",
    "Familiar with IDEs like VS Code, IntelliJ, and PyCharm.",
    "Knowledge of testing frameworks and TDD practices.",
    
    # Industry Experience
    "5+ years of experience in software development and system architecture.",
    "Experience working in fast-paced startup environments.",
    "Background in fintech with knowledge of payment processing systems.",
    "Experience in e-commerce platforms and customer-facing applications.",
    "Knowledge of cybersecurity best practices and secure coding standards.",
    
    # Education & Certifications
    "Bachelor's degree in Computer Science or related field.",
    "Certified AWS Solutions Architect with hands-on cloud experience.",
    "Completed advanced courses in machine learning and data science.",
    "Active participation in open-source projects and tech communities.",
    
    # Leadership & Innovation
    "Led technical initiatives that improved system performance by 40%.",
    "Mentored 5+ junior developers and conducted technical interviews.",
    "Introduced new technologies that reduced development time by 30%.",
    "Experience with technical architecture decisions and system design.",
    
    # Research & Development
    "Published research papers in machine learning and computer vision.",
    "Experience with cutting-edge technologies like blockchain and IoT.",
    "Contributed to open-source projects with 1000+ GitHub stars.",
    "Experience with research and development in emerging technologies.",
]

# Setup
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection(name="resume_blocks")

for i, text in enumerate(resume_blocks):
    embedding = embed_model.encode(text).tolist()
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[str(i)]
    )

print("✅ Resume data added to ChromaDB!")
print(f"📊 Total resume blocks loaded: {len(resume_blocks)}")