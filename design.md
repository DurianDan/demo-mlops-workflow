## reference:
- [AIHUB][1]
-  [[MLOps Crash Course] Seminar 01 - MLOps Platform][2] 
    - Storage: PostgreSQL (can store JSON - first time receive)
      - features: EAV dynamic schema design
      - ML metadata: 
      - raw-data: EAV
        - meta_id: raw-data-metadata id
        - artribute: string
        - value_type: string
        - value: string
      - raw-data-metadata
    - Data Pipeline ( Airflow ): Concurrent **saving raw** and **generate features** at the same time.

- TODO:  
## Design
### stage 1 (training)
- Save data to unresolved-data `/resolve-data/`
- Check scheme directly
- Make request to move unresolved data to raw-data
- Design Schemas for raw-data
- get raw-data metadata, drift determinator field

### stage 2 (deploy)
- Data saved in 
- Get data
- Save on MySQL server
- Metadata detection:
  - Data drift detection




[1]:https://aihub.ml/competitions/376
[2]:https://www.youtube.com/watch?v=gsLezXRGeSg&t=1385s