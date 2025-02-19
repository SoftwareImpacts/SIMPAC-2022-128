# SMIRK Documentation

The following documents are available in this folder.

- [System Requirements Specification](</docs/System Requirements Specification.md>) (SRS)
- [Data Management Specification](</docs/Data Management Specification.md>) (DMS)
- [System Architecture Description](https://github.com/RI-SE/smirk/blob/main/docs/System%20Architecture%20Description.md) (SAD)
- [Machine Learning Component Specification](</docs/ML Component Specification.md>) (MLCS)
- [System Test Specification](</docs/System Test Specification.md>) (STS)
- [Deployment Specification](</docs/Deployment Specification.md>) (DS)

Supplementary documents
- [Numbered ALTAI questions](</docs/support/ALTAI_Numbered_Questions_v1.0.pdf>) from the Assessment List for Trustworthy Artificial Intelligence. The European Commission published ALTAI to support self-assessment. The questions were discussed in a related paper on [AI ethics](https://arxiv.org/abs/2103.09051).
- [Instructions for data generation](https://github.com/RI-SE/smirk/blob/main/docs/generate_data.md). Note that ESI Pro-SiVIC is needed to reproduce the SMIRK data set.

## Safety Assurance

SMIRK evolves in compliance with [Guidance on the Assurance of Machine Learning in Autonomous Systems](https://www.york.ac.uk/assuring-autonomy/guidance/amlas/) (AMLAS) published by the University of York. The figure below shows an overview of the AMLAS process and the six corresponding stages. 

![AMLAS process](/docs/figures/amlas_process.png) <a name="amlas"></a>

The table below is an index to navigate the artifacts mandated (cf. [ID]) by the AMLAS process. The input/output columns indicate in which AMLAS stage the artifact is used. The final column lists the location of the corresponding artifact for SMIRK.

The set of artifacts listed constitutes the safety case for the ML-based object detection component of SMIRK, i.e., it instantiates the [ML Assurance Scoping Pattern](</docs/System Requirements Specification.md#ml_assurance_scoping_pattern>).

|      ID   |     Title                                        |     Input to    |     Output from    |     Where?       |     Status       |
|:---------:|--------------------------------------------------|:---------------:|:------------------:|------------------|------------------|
|     [A]   |     System Safety Requirements                     |         1, 6    |                    | [SRS Sec 3.1](</docs/System Requirements Specification.md#31-system-safety-requirements-a->)    | Up-to-date v0.99 |
|     [B]   |     Description of Operating Environment of System |         1, 6    |                    | [SRS Sec 4](</docs/System Requirements Specification.md#4-operational-design-domain-b->)    | Up-to-date v0.99 |
|     [C]   |     System Description                             |         1, 6    |                    | [SRS Sec 2](</docs/System Requirements Specification.md#2-system-description-c->)    | Up-to-date v0.99 |
|     [D]   |     ML Component Description                       |          1      |                    | [MLCS Sec 2](</docs/ML Component Specification.md#2-ml-component-description-d>)    | Up-to-date v0.99 |
|     [E]   |     Safety Requirements Allocated to ML Component  |          2      |            1       | [SRS Sec 3.2](</docs/System Requirements Specification.md#32-safety-requirements-allocated-to-ml-component-e->)    | Up-to-date v0.99 |
|     [F]   |     ML Assurance Scoping Argument Pattern          |          1      |                    | [SRS Sec 5](</docs/System Requirements Specification.md#5-ml-assurance-scoping-argument-pattern-f->)    | Up-to-date v0.99 |
|     [G]   |     ML Safety Assurance Scoping Argument           |                 |            1       | [SRS Sec 6](</docs/System Requirements Specification.md#6-ml-safety-assurance-scoping-argument-g->)    | Up-to-date v0.99 |
|     [H]   |     ML Safety Requirements                         |       3, 4, 5   |            2       | [SRS Sec 3.3](</docs/System Requirements Specification.md#33-machine-learning-safety-requirements-h->) | Up-to-date v0.99 |
|     [I]   |     ML Safety Requirements Argument Pattern        |          2      |                    | [SRS Sec 7](</docs/System%20Requirements%20Specification.md#7-ml-safety-requirements-argument-pattern-i->) | Up-to-date v0.99 |
|     [J]   |     ML Safety Requirements Validation Results      |                 |            2       | [SRS Sec 8](</docs/System%20Requirements%20Specification.md#8-ml-safety-requirements-validation-results-j->) | Up-to-date v0.99 |
|     [K]   |     ML Safety Requirements Argument                |                 |            2       | [SRS Sec 9](</docs/System%20Requirements%20Specification.md#9-ml-safety-requirements-argument-k->) | Up-to-date v0.99 |
|     [L]   |     Data Requirements                              |                 |            3       | [DMS Sec 2](</docs/Data Management Specification.md#data_rqts>) | Up-to-date v0.99 |
|     [M]   | Data Requirements Justification Report             |                 |          3         | [DMS Sec 3](</docs/Data Management Specification.md#data_rqts_just>) | Up-to-date v0.99 |
|     [N]   | Development Data                                   |                 |          3         | [AI Sweden](https://www.ai.se/en/data-factory/datasets/smirk-synthetic-pedestrians-dataset) | Up-to-date v0.99 |
|     [O]   | Internal Test Data                                 |                 |          3         | [AI Sweden](https://www.ai.se/en/data-factory/datasets/smirk-synthetic-pedestrians-dataset) | Up-to-date v0.99 |
|     [P]   | Verification Data                                  |                 |          3         | [AI Sweden](https://www.ai.se/en/data-factory/datasets/smirk-synthetic-pedestrians-dataset) | Up-to-date v0.99 |
|     [Q]   | Data Generation Log                            |                 |            3       | [DMS Sec 4](</docs/Data Management Specification.md#data_gen>) | Up-to-date v0.99 |
|     [R]   | ML Data Argument Pattern                           |        3        |                    | [DMS Sec 5](</docs/Data Management Specification.md#data_argument_pattern>) | Up-to-date v0.99 |
|     [S]   | ML Data Validation Results                         |                 |          3         | [DMS Sec 6](</docs/Data Management Specification.md#data_validation_results>) | Up-to-date v0.99 |
|     [T]   | ML Data Argument                                   |                 |          3         | [DMS Sec 7](</docs/Data Management Specification.md#data_argument>) | Up-to-date v0.99 |
|     [U]   | Model Development Log                          |                 |          4         | [MLCS Sec 3](</docs/ML%20Component%20Specification.md#3-model-development-log-u>) | Up-to-date v0.99 |
|     [V]   | ML Model                                           |       5, 6      |          4         | [Model](https://github.com/RI-SE/smirk/releases/download/v0.99/pedestrian-detection-model.pt) | Up-to-date v0.99 |
|     [W]   | ML Learning Argument Pattern                   |          4      |                    | [MLCS Sec 5](</docs/ML%20Component%20Specification.md#5-ml-model-learning-argument-pattern-w>) | Up-to-date v0.99 |
|     [X]   | Internal Test Results                          |                 |            4       | [Protocols](https://github.com/RI-SE/smirk/blob/main/docs/protocols/Internal%20Test%20Results%20[X]%202022-06-16.pdf) | Up-to-date v0.99 |
|     [Y]   | ML Learning Argument                           |                 |            4       | [MLCS Sec 6](</docs/ML%20Component%20Specification.md#6-ml-learning-argument-y>) | Up-to-date v0.99 |
|     [Z]   | ML Verification Results                        |                 |            5       | [Protocols](https://github.com/RI-SE/smirk/blob/main/docs/protocols/ML%20Verification%20Results%20[Z]%202022-06-16.pdf) | Up-to-date v0.99 |
|     [AA]  | Verification Log                               |                 |            5       | [STS Sec 3](</docs/System%20Test%20Specification.md#3-ml-model-testing-aa>) | Up-to-date v0.99 |
|     [BB]  | ML Verification Argument Pattern               |          5      |                    | [STS Sec 5](</docs/System%20Test%20Specification.md#5-ml-verification-argument-pattern-bb>) | Up-to-date v0.99 |
|     [CC]  | ML Verification Argument                       |                 |            5       | [STS Sec 6](</docs/System%20Test%20Specification.md#6-ml-verification-argument-cc>) | Up-to-date v0.99 |
|     [DD]  | Erroneous Behaviour Log                        |                 |            6       | [DS Sec 4](</docs/Deployment%20Specification.md#4-erroneous-behaviour-log-dd>) | Up-to-date v0.99 |
|     [EE]  | Operational Scenarios                          |         6       |                    | [STS Sec 4.1](</docs/System%20Test%20Specification.md#41-operational-scenarios-ee>) | Up-to-date v0.99 |
|     [FF]  | Integration Testing Results                        |                 |          6         | [Protocols](https://github.com/RI-SE/smirk/blob/main/docs/protocols/Integration%20Testing%20Results%20[FF]%202022-06-16.pdf) | Up-to-date v0.99 |
|     [GG]  | ML Deployment Argument Pattern                     |        6        |                    | [DS Sec 5](</docs/Deployment%20Specification.md#5-ml-deployment-argument-pattern-gg>) | Up-to-date v0.99 |
|     [HH]  | ML Deployment Argument                         |                 |            6       | [DS Sec 6](</docs/Deployment%20Specification.md#6-ml-deployment-argument-hh>) | Up-to-date v0.99 | 
