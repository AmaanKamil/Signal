# Careem AI Challenge Submission: Signal

**Project Name**: Signal
**Tagline**: Turning behavior into product decisions.

**Public App Link**: [https://signal-careem.streamlit.app/](https://signal-careem.streamlit.app/)
**GitHub Repository**: [https://github.com/AmaanKamil/Signal](https://github.com/AmaanKamil/Signal)

## Product Description
Signal is an AI-native Product Intelligence Platform designed to automate the work of Product Managers and Data Analysts. Instead of just showing dashboards, Signal *reasons* about data to identify friction points, suggest features, and design experiments automatically.

## How it uses AI
Signal uses a multi-stage AI pipeline:
1.  **Pattern Recognition**: Rule-based logic first scans user behavior (sessions, conversion, drops) to find "signals".
2.  **Strategic Reasoning**: GPT-4o interprets these signals to explain *why* users are churning or converting.
3.  **Generative Design**: The AI proposes concrete product features and designs A/B tests to validate them.
4.  **Prioritization**: The AI acts as a Head of Product, ranking initiatives by Impact/Effort to build a roadmap.

## Key Features
- **Executive Health Dashboard**: Instant view of product vitals.
- **Automated Root Cause Analysis**: Identifies funnel leaks without manual digging.
- **Generative Roadmap**: Go from raw data to a prioritized feature list in 1 click.
- **Experiment Designer**: Auto-generates hypothesis and success metrics.

## Tech Stack
- Python / Streamlit
- OpenAI GPT-4o
- Pandas / Plotly

## Testing Instructions
1.  Launch the app or access the [Live Demo](https://signal-careem.streamlit.app/).
2.  Click **"Load Sample Dataset"** in the sidebar to populate the dashboard with Careem-like user behavior data.
3.  Enter an **OpenAI API Key** in the sidebar.
4.  Click **"Generate AI Report"** to see the AI build a product strategy live.
5.  Navigate through the tabs (**Insights**, **Features**, **Roadmap**) to see the results.
