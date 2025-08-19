import streamlit as st
import os
from datetime import datetime


def get_environment():
    """Determine the current environment based on environment variables or branch"""
    env = os.getenv("ENVIRONMENT", "dev").lower()
    return env


def get_environment_config(env):
    """Get environment-specific configuration"""
    configs = {
        "dev": {
            "title": "Dev Environment",
            "bg_color": "#2E7D32",  # Green
            "text_color": "#FFFFFF",
            "icon": "🔧",
            "description": "Development Environment - Latest features under development",
        },
        "qa": {
            "title": "QA Environment",
            "bg_color": "#F57F17",  # Yellow/Orange
            "text_color": "#000000",
            "icon": "🧪",
            "description": "Quality Assurance Environment - Testing and validation",
        },
        "prod": {
            "title": "Production Environment",
            "bg_color": "#C62828",  # Red
            "text_color": "#FFFFFF",
            "icon": "🚀",
            "description": "Production Environment - Live application",
        },
    }
    return configs.get(env, configs["dev"])


def apply_custom_css(config):
    """Apply custom CSS based on environment"""
    st.markdown(
        f"""
    <style>
    .main > div {{
        background-color: {config['bg_color']};
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }}

    .stApp > header {{
        background-color: transparent;
    }}

    .environment-header {{
        background-color: {config['bg_color']};
        color: {config['text_color']};
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        font-size: 1.5rem;
    }}

    .environment-info {{
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: {config['text_color']};
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def main():
    # Get environment configuration
    current_env = get_environment()
    config = get_environment_config(current_env)

    # Set page config
    st.set_page_config(
        page_title=config["title"],
        page_icon=config["icon"],
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Apply custom styling
    apply_custom_css(config)

    # Environment header
    st.markdown(
        f"""
    <div class="environment-header">
        {config['icon']} {config['title']} {config['icon']}
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Main content
    st.title(f"Welcome to {config['title']}")
    st.write(config["description"])

    # Environment information
    st.markdown(
        f"""
    <div class="environment-info">
        <h3>Environment Information</h3>
        <p><strong>Current Environment:</strong> {current_env.upper()}</p>
        <p><strong>Deployment Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
        <p><strong>Version:</strong> {os.getenv('GITHUB_SHA', 'local')[:8]}</p>
        <p><strong>Branch:</strong> {os.getenv('GITHUB_REF_NAME', 'local')}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Sidebar with additional info
    with st.sidebar:
        st.header("🔧 Environment Details")
        st.write(f"**Environment:** {current_env.upper()}")
        st.write(
            f"**Status:** {'🟢 Active' if current_env == 'prod' else '🟡 Testing' if current_env == 'qa' else '🔵 Development'}"
        )

        if current_env == "dev":
            st.info(
                "🔧 This is the development environment. New features are tested here."
            )
        elif current_env == "qa":
            st.warning(
                "🧪 This is the QA environment. Features are validated here before production."
            )
        elif current_env == "prod":
            st.success(
                "🚀 This is the production environment. Stable, tested features only."
            )

    # Feature demonstration section
    st.header("🚀 Application Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📊 Data Display")
        if st.button("Generate Sample Data"):
            import random

            data = {
                "Metric": ["Users", "Revenue", "Performance"],
                "Value": [random.randint(100, 1000) for _ in range(3)],
            }
            st.table(data)

    with col2:
        st.subheader("🎯 Environment Test")
        if st.button("Test Environment"):
            st.success(f"✅ {config['title']} is working correctly!")
            st.balloons()

    with col3:
        st.subheader("📈 Metrics")
        if current_env == "prod":
            st.metric("Uptime", "99.9%", "0.1%")
        elif current_env == "qa":
            st.metric("Test Coverage", "85%", "5%")
        else:
            st.metric("Features", "12", "3")

    # Footer
    st.markdown("---")
    st.markdown(
        f"""
    <div style="text-align: center; color: {config['text_color']}; opacity: 0.7;">
        <p>🔄 CI/CD Pipeline Demo • Environment: {current_env.upper()} • 
        Deployed via GitHub Actions {config['icon']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
