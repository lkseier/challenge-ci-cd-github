# 🚀 CI/CD GitHub Actions Demo

A comprehensive CI/CD pipeline demonstration using GitHub Actions with multi-environment deployment simulation.

## 📋 Project Overview

This project demonstrates a complete DevOps workflow with:
- **Continuous Integration (CI)**: Automated testing and building on every code change
- **Continuous Deployment (CD)**: Automated deployment to Dev, QA, and Production environments
- **Environment Management**: Different configurations for each environment
- **Approval Gates**: Production deployments require manual approval

## 🎯 Learning Objectives

- ✅ Understand GitHub Actions workflows
- ✅ Implement automated build & test jobs (CI)
- ✅ Simulate deployments to multiple environments (CD)
- ✅ Use GitHub Environments & approvals
- ✅ Work with branches and branch protections

## 🏗️ Architecture

### **CI Pipeline** (`.github/workflows/ci.yml`)
```
Pull Request → Lint → Test → Build → Artifacts
```

### **CD Pipeline** (`.github/workflows/cd.yml`)
```
Push to dev  → Deploy to Development
Push to qa   → Deploy to QA
Push to main → Deploy to Production (with approval)
```

## 📁 Repository Structure

```
challenge-ci-cd-github/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── app/                         # Application code
│   └── main.py                 # Streamlit app entry point
├── tests/                       # Test suite
│   └── test_app.py             # Unit tests
└── .github/workflows/          # GitHub Actions
    ├── ci.yml                  # Continuous Integration
    └── cd.yml                  # Continuous Deployment
```

## 🚀 Getting Started

### **Prerequisites**
- Python 3.12.3
- Git
- GitHub account

### **Local Development Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/challenge-ci-cd-github.git
   cd challenge-ci-cd-github
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app locally:
   ```bash
   streamlit run app/main.py
   ```

5. Run tests:
   ```bash
   pytest tests/ -v
   ```

## 🔄 How to Trigger CI/CD

### **Continuous Integration (CI)**
CI runs automatically on:
- **Pull Requests** to `main` branch
- **Direct pushes** to `main`, `dev`, or `qa` branches

**What CI does:**
1. 🔍 **Lint**: Code quality checks with flake8 and black
2. 🧪 **Test**: Run unit tests with pytest
3. 🔨 **Build**: Create build artifacts
4. 📦 **Upload**: Store test results and build artifacts

### **Continuous Deployment (CD)**
CD runs automatically on:
- **Push to `dev`** → Deploys to Development environment
- **Push to `qa`** → Deploys to QA environment  
- **Push to `main`** → Deploys to Production environment (requires approval)

## 🌍 Environments

### **Development Environment** 🔧
- **Trigger**: Push to `dev` branch
- **Auto-deploy**: Yes
- **Approval**: Not required
- **UI**: Green background, "Dev Environment" title

### **QA Environment** 🧪
- **Trigger**: Push to `qa` branch
- **Auto-deploy**: Yes
- **Approval**: Not required
- **UI**: Yellow background, "QA Environment" title

### **Production Environment** 🚀
- **Trigger**: Push to `main` branch
- **Auto-deploy**: No (requires approval)
- **Approval**: Required
- **UI**: Red background, "Production Environment" title

## 🔧 Environment Configuration

The Streamlit app automatically detects the environment using the `ENVIRONMENT` variable and displays:
- Environment-specific styling (colors, icons)
- Deployment information (branch, commit SHA, timestamp)
- Environment status and health checks

## 📝 Workflow Examples

### **Feature Development Workflow**
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push and create PR
git push origin feature/new-feature
# → Triggers CI workflow

# After PR approval, merge to main
# → Triggers CD workflow for Production (with approval)
```

### **Development Testing Workflow**
```bash
# Work on dev branch
git checkout dev
git add .
git commit -m "Update dev features"
git push origin dev
# → Triggers CD workflow for Development environment
```

### **QA Testing Workflow**
```bash
# Promote to QA
git checkout qa
git merge dev
git push origin qa
# → Triggers CD workflow for QA environment
```

## 🔐 Required Secrets

Set up these secrets in GitHub Settings → Secrets and variables → Actions:

### **Environment Secrets:**
- `DEV_SECRET`: Development environment credentials
- `QA_SECRET`: QA environment credentials  
- `PROD_SECRET`: Production environment credentials
- `PROD_API_KEY`: Production API key

## 📊 Example Workflow Logs

### **Successful CI Run:**
```
✅ Lint completed - Code quality checks passed
✅ Tests completed - 8/8 tests passed (100% coverage)
✅ Build completed - Artifacts uploaded
```

### **Successful CD Run (Dev):**
```
🚀 Deploying to Development environment...
📦 Preparing dev deployment...
🔧 Configuring dev environment...
🌐 Starting dev server...
🚀 Deployed to 'Development'
✅ Dev deployment completed successfully!
```

### **Production Deployment (with Approval):**
```
⏳ Waiting for approval from repository administrators...
✅ Approval received from @username
🚀 Deploying to Production environment...
[... deployment steps ...]
🚀 Deployed to 'Production'
🎉 Production deployment completed successfully!
```

## 🧪 Testing

Run the test suite locally:
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html

# Run specific test
pytest tests/test_app.py::TestEnvironmentConfig::test_get_environment_default -v
```

## 🛠️ Troubleshooting

### **Common Issues:**

1. **Workflow not triggering:**
   - Check branch names match exactly (`dev`, `qa`, `main`)
   - Ensure workflows are in `.github/workflows/` directory

2. **Tests failing:**
   - Verify Python version compatibility
   - Check all dependencies are in `requirements.txt`

3. **Environment deployment failing:**
   - Verify environment secrets are set correctly
   - Check environment names match workflow configuration

4. **Production approval not working:**
   - Ensure "Required reviewers" is enabled in Production environment
   - Add yourself as a required reviewer

## 📈 Next Steps

After setting up this project, you can extend it with:
- Database migrations in deployment steps
- Blue-green deployment strategies
- Rollback mechanisms
- Performance testing
- Security scanning
- Slack/Email notifications

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests locally: `pytest tests/ -v`
4. Create a pull request
5. Wait for CI to pass
6. Get approval and merge

## 📄 License

This is a learning project for CI/CD practice.

---

**Built with ❤️ for learning DevOps and GitHub Actions**