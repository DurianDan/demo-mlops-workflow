### Data Engineering
#### 1. Project Structure
- `api`: receive and response to MLOpsVN's requests
  - `problem`
    - `api_models`: Define `model` classes, to interact with SQL tables.
      - `base.py`: define `Base`, a base class for all models to inherit 
      - `factory`: create Specific model based on phase_id and prob_id
  - `schema`: define request/response body 

### Data Scientist-ing
- To serve a model, put the model in this folder: **flow**/**api**/**predict**/**MLmodels**
  - E.g.: to save model `sample.model.file` in **phase 2**, to solve **problem 3**
    ```bash
    flow/api/predict/ml_models/phase2/prob3/
    ```
