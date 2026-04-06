# Mock Trial AI V2

## Table of Contents
* [Project Overview](#project-overview)
* [Features](#features)
* [Usage Guide](#usage-guide)
* [Technical Challenges & Limitations](#technical-challenges--limitations)
* [The Road to V3: Future Work](#the-road-to-v3-future-work)
* [Real-World Impact](#real-world-impact)
* [Contributing](#contributing)
* [License](#license)

## Project Overview
V2 represents the research and prototype phase of this project, focusing on the feasibility of using Small Language Models (SLMs) for legal reasoning. This version was built using the **Phi-1.5 model (1.3B parameters)** to test how a lightweight architecture handles the complex demands of courtroom simulation and automated legal coaching.

## Features
* **Case Analysis Prototype:** Fine-tuned to act as a Senior Prosecutor/Defender, extracting 3 specific pieces of physical evidence from legal packets.
* **Witness Roleplay:** Established basic witness interactions and deponent personas based on provided affidavits.
* **Objection Checker:** A specialized module designed to scan user-generated trial materials for compliance with the Rules of Evidence.
* **Feature Pivot (Objection Practice):** An experimental "Objection Game" was prototyped but ultimately deprecated. It was determined that legal objections are too context-dependent for an SLM to replicate accurately, and students benefit more from in-person practice for these specific interpersonal skills.

## Usage Guide
To utilize this prototype, the user must set up an environment with GPU support (NVIDIA T4 or higher). After installing the necessary dependencies listed in `requirements.txt`, the user can run the provided notebook to initiate the Phi-1.5 engine and upload PDF case materials for parsing.

## Technical Challenges & Limitations
Development of V2 revealed a **Reasoning Plateau** inherent in the 1.3B parameter architecture. While the model was fast, it lacked the cognitive depth required for high-level legal logic. A significant hurdle was **data fragmentation**; the initial training data was experimental and unorganized, leading to inconsistent performance. Furthermore, the model struggled with a limited context window, making it difficult to process full-length legal packets without losing critical information from earlier pages.

## The Road to V3: Future Work
The limitations identified in V2 directly dictated the strategy for Version 3. To create a truly usable and professional-grade tool, the project has transitioned to the **Llama-3.1-8B architecture**, providing a six-fold increase in parameter count and a massive expansion of the effective context window. 

A primary focus for V3 is **Data Streamlining**. By utilizing **Perplexity AI as a 'Teacher Model'** to synthesize organized, factually dense "Gold Standard" datasets, V3 replaces the experimental noise of V2 with a strictly structured legal framework. This "Teacher-Student" distillation ensures that the model can handle complex "Criminal Intent" logic and personality-driven witness simulations with high reliability.

## Real-World Impact
Despite its technical limitations, V2 served as a vital proof of concept. It provided the data processing pipeline and architectural lessons necessary to evolve the project from a research experiment into a high-performance legal tool used by active mock trial competitors.

## License
This project is distributed under the MIT License. See the LICENSE file for more information.
