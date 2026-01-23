# Signal: Product Intelligence Platform

**Turning behavior into product decisions.**

Signal is an AI-powered product intelligence system designed to transform raw user behavior data into actionable product strategies. Built for the Careem ecosystem, it combines deterministic pattern detection with generative AI to identify risks, spot opportunities, and design data-driven roadmaps.

## 🚀 Key Features

### 1. Unified Health Dashboard
A command-center view of your product's vitals, offering instant production-grade metrics on Engagement, Conversion, Retention, and Monetization.

### 2. Intelligent Pattern Detection
Signal automatically scans millions of events to detect behavioral patterns:
- **Friction Points**: High-intent users failing to convert.
- **Churn Risk**: Loyal users showing declining engagement.
- **Ecosystem Growth**: Single-service users ripe for cross-selling.

### 3. Generative Strategy Engine
Powered by LLMs, Signal goes beyond analytics to generate strategy:
- **Strategic Insights**: Narrative explanations of *why* metrics are changing.
- **Feature Ideation**: Concrete feature proposals to solve detected problems.
- **Experiment Design**: rigorous A/B test plans to validate features.
- **Roadmap Prioritization**: AI-ranked initiatives based on Impact vs. Effort.

## 🛠 Architecture

Signal operates on a hybrid intelligence architecture:
- **Data Engine**: Pandas-based processing layer for cleaning and aggregation.
- **Intelligence Engine**: Rule-based logic for deterministic pattern detection.
- **AI Engine**: Modular LLM integration for reasoning and generation.
- **UI Layer**: Enterprise-grade Streamlit interface for decision makers.

## 💻 Tech Stack
- **Frontend**: Streamlit + Custom CSS
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly Express
- **AI/LLM**: OpenAI GPT-4o
- **Language**: Python 3.10+

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API Key (for Generative AI features)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/signal.git
   cd signal
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

### Configuration
To enable AI features, you can either enter your API key in the sidebar or set it in `.streamlit/secrets.toml`:

```toml
[openai]
api_key = "sk-your-key-here"
```

## 📂 Project Structure
```
signal/
├── ai/                 # Generative AI Engines
├── components/         # Legacy Components
├── data/               # Datasets
├── docs/               # Documentation
├── ui/                 # Modern UI Layer
│   ├── components/     # Atomic UI Elements
│   ├── pages/          # App Pages
├── utils/              # Data & Intelligence Utilities
├── app.py              # Entry Point
└── requirements.txt    # Dependencies
```

## 🛡 Security & Privacy
Signal is designed with privacy in mind. Data processing happens locally within the application instance. When using AI features, only aggregated, non-PII summaries are sent to the LLM for reasoning.

## 📝 License
MIT License. Created for the Careem AI Engineering Challenge.
