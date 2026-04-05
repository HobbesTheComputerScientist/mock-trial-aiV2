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
Mock Trial AI V2 represents the research and prototype phase of this project, focusing on the feasibility of using Small Language Models (SLMs) for legal reasoning. This version was built using the Phi-1.5 model (1.3 billion parameters) to test how a lightweight architecture could handle the complex demands of courtroom simulation. The primary goal of V2 was to experiment with diverse training data structures and establish a baseline for automated legal coaching.

## Features
The V2 prototype included several core modules designed to assist mock trial competitors. The Case Analysis feature allowed for basic fact extraction from legal packets, while the Objection Simulator creates questions and has users flag potentially objectionable questions. Additionally, the project featured a Objection Checker to check user-generated content for compliance with the Rules of Evidence and a Witness Simulator that attempted to roleplay personas based on provided affidavits.

## Usage Guide
To utilize this prototype, the user must set up a environment with GPU support, specifically an NVIDIA T4 or higher. After installing the necessary dependencies listed in the requirements file, the user can run the provided notebook to initiate the Phi-1.5 engine. Once active, the user can upload PDF case materials which the system parses to provide the context necessary for analysis and interaction.

## Technical Challenges and Limitations
Development of V2 revealed significant hurdles inherent in the Phi-1.5 architecture. The most prominent issue was the lack of reasoning depth; while the model was exceptionally fast, it struggled with the nuanced logic required for high-level legal arguments. Hallucinations were common, with the model frequently inventing legal precedents or facts not found in the source text. Despite extensive efforts in prompt engineering, I encountered a plateau where the model's small parameter count simply could not support the level of accuracy required for reliable legal work.

## The Road to V3: Future Work
The limitations identified in V2 directly informed the development strategy for Version 3. To overcome the reasoning gaps and hallucination issues, the project has transitioned to the Llama-3.1-8B architecture. This move provides a six-fold increase in parameter count, allowing for significantly more robust cognitive processing. A primary focus for V3 is expanding the effective context window to ensure the model can ingest and retain information from full-length legal packets without truncation or memory loss. Furthermore, V3 replaces the experimental data mixes of V2 with a strictly organized, domain-specific legal dataset, utilizing Unsloth and 4-bit quantization to maintain efficiency.

## Real-World Impact
Despite its technical limitations, V2 served as a vital proof of concept that validated the demand for accessible legal coaching tools. It provided a functional interface and a data processing pipeline that proved students could benefit from an automated system when professional attorney-coaches are unavailable. The lessons learned regarding data quality and model scale were instrumental in evolving the project into a professional-grade tool.

## Contributing
This repository is maintained as an archived research prototype to document the project's evolution. For the active, stable version of the Mock Trial AI, please refer to the V3 repository. Feedback on the research methodology and data experimentation used in this version is always welcome.

## License
This project is distributed under the MIT License. See the LICENSE file for more information.
