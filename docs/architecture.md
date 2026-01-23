# Signal Core Architecture

Signal is built on a modular "Layered Intelligence" architecture designed to separate data processing from strategic reasoning.

## 1. Data Layer (`utils/data_engine.py`)
Responsible for ingestion, cleaning, and normalization.
- **Input**: Raw CSV data (User Behavior Dataset).
- **Processing**: Type casting, null handling, schema validation.
- **Output**: `processed_df` stored in session state.

## 2. Intelligence Layer (`utils/intelligence_engine.py`)
A deterministic rule-engine that scans the processed data for known behavioral patterns.
- **Pattern Modules**:
  - `detect_engagement_patterns`: Identifies power users vs. zombies.
  - `detect_friction_patterns`: Identifies funnel leakage.
  - `detect_ecosystem_patterns`: Identifies cross-vertical usage.
- **Output**: Structured `Intelligence` object containing lists of Problems and Opportunities.

## 3. AI Layer (`ai/orchestrator.py`)
A generative engine that consumes the deterministic intelligence to produce creative strategy.
- **Insight Engine**: Synthesizes patterns into narrative insights.
- **Feature Engine**: Proposes solutions for detected problems.
- **Experiment Engine**: Designs validation tests.
- **Priority Engine**: Ranks initiatives.

## 4. UI Layer (`ui/`)
A decoupled frontend built for executive consumption.
- **Atomic Components**: Cards, Badges, Metrics.
- **Pages**: Specialized dashboards (Overview, Insights, Roadmap).
