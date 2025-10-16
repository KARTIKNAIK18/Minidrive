 <h1 align="center">MiniDrive </h1>

<p align="center">
  <img src="images/drive.jpg" alt="MiniDrive Banner" style="width:75%; height:250px; display:block;"
</p>

<p align="center">
  <strong>A lightweight, serverless file storage web application built with Django & AWS</strong>
</p>



## 🏗️ Architecture
```
MiniDrive follows a modular, serverless design:
┌────────────────────────────────────────────────────────────┐                        
│                     User Interface                         │    
│                                                            │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                    AWS API Gateway                         │
│     (Handles routing, authentication, and throttling)      │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                  AWS Lambda Functions                      │
│     (Serverless backend logic for file operations)         │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                      AWS S3 Bucket                         │
│     (Stores files securely with presigned URL access)      │
└────────────────────────────────────────────────────────────┘

```

- 🖥️ **Frontend**: Django handles UI and routing
- 🔌 **API Gateway**: Manages RESTful endpoints and auth
- 🧠 **Lambda**: Executes file operations
- 🗄️ **S3**: Stores files securely with presigned access

<!-- <p align="center">
  <img src="docs/architecture-diagram.png" alt="MiniDrive Architecture" width="600">
</p> -->

## ⚙️ Setup

### 🧰 Prerequisites

- Python 3.8+
- pip
- Git
- AWS Account

### 🧪 Local Development

```bash
# 1. Clone the repo
git clone https://github.com/KARTIKNAIK18/Minidrive.git
cd minidrive

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add environment variables
echo "API_URL=https://szudj39ivk.execute-api.ap-south-1.amazonaws.com/dev/files" > .env

# 5. Run migrations
python manage.py migrate

# 6. Start server
python manage.py runserver
```

🔗 Visit: `http://127.0.0.1:8000`

---

## 📝 Usage

### 📤 Upload Files

1. Go to the upload page
2. Drag & drop or browse files
3. Click **Upload**
4. View files in your drive

### 📁 Manage Files

- 🖼️ View: All files listed on homepage
- 📥 Download: Click to download
- 👤 User authentication: on goning***

---

## 🚀 Deployment


### ☁️ AWS Serverless Setup

1. Deploy Lambda functions
2. Configure API Gateway
3. Create S3 buckets
4. Set IAM roles & permissions

---

## 📈 Future Enhancements

- 🔐 User authentication
- 🔗 File sharing
- 🗂️ Folder organization
- 🔍 Search functionality
- 🕒 File versioning

---

## 📜 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
   <a href="https://github.com/KARTIKNAIK18">KARTIK NAIK</a>
</p>
