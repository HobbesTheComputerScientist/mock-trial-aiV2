# Mock Trial AI V2: The Research & Fine-Tuning Phase

## Table of Contents
* [Project Overview](#project-overview)
* [Features](#features)
* [Usage Guide](#usage-guide)
* [Technical Challenges & Limitations](#technical-challenges--limitations)
* [The Road to V3: Future Work](#the-road-to-v3-future-work)
* [Metrics & Model Traction](#metrics--model-traction)
* [License](#license)

## Project Overview
V2 represents the research and prototype phase, focusing on the feasibility of using Small Language Models (SLMs) for legal reasoning. Built using **Phi-1.5 (1.3B parameters)**, this version moved from simple prompting to active model training.

## Features
* **Case Analysis Prototype:** Fine-tuned to act as a Senior Prosecutor/Defender.
* **Objection Checker:** Scans user content for Rules of Evidence compliance.
* **Feature Pivot:** Deprecated the "Objection Practice" game to focus on higher-utility tools.

## Technical Challenges & Limitations
Phi-1.5 revealed a **Reasoning Plateau**. Initial training data was experimental and unorganized. To solve this, I began using **Perplexity AI as a 'Teacher Model'** to generate more streamlined datasets, though the 1.3B architecture still struggled with complex context windows and legal nuances.

## Metrics & Model Traction
The research conducted in V2 gained significant attention within the AI developer community:
* **Training Dataset:** Successfully reached **57 downloads** on Hugging Face.
* **Proof of Concept:** Validated that specialized legal SLMs can outperform general models when properly aligned.

## The Road to V3: Future Work
V2 informed the transition to **Llama-3.1-8B**. By moving to a larger parameter count and a more organized "Teacher-Student" data pipeline, the project aimed to solve the reasoning gaps identified in this version.

## License
Distributed under the MIT License.
