# 🚀 Serverless IoT Analytics Lakehouse on AWS

> **A production-grade, serverless IoT data analytics platform built on AWS to ingest, process, transform, and analyze real-time sensor data using modern cloud-native services.**

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![Glue](https://img.shields.io/badge/AWS-Glue-orange)
![Athena](https://img.shields.io/badge/AWS-Athena-orange)
![QuickSight](https://img.shields.io/badge/AWS-QuickSight-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

This project demonstrates how to build a **highly scalable, event-driven IoT analytics platform** capable of processing millions of IoT sensor events using a completely serverless architecture.

Incoming IoT device data is securely ingested through **AWS IoT Core**, processed by **AWS Lambda**, stored in an **Amazon S3 Data Lake**, transformed using **AWS Glue**, queried with **Amazon Athena**, and visualized using **Amazon QuickSight**.

The architecture eliminates infrastructure management while providing scalability, cost efficiency, and real-time analytics capabilities.

---

# ✨ Features

- ⚡ Real-Time IoT Data Ingestion
- 🔒 Secure MQTT Communication
- ☁️ Fully Serverless Architecture
- 📊 Real-Time Analytics Dashboard
- 📦 Data Lake using Amazon S3
- 🔄 Automated ETL Pipelines
- 📈 SQL Analytics using Athena
- 📉 Interactive QuickSight Dashboards
- 📁 Partitioned Parquet Storage
- 📜 Schema Discovery using Glue Crawlers
- 🚨 CloudWatch Monitoring & Logging
- 🔁 Automatic Retry Mechanism
- 📬 Dead Letter Queue Support
- 🔐 IAM Least Privilege Security
- ⚙ Infrastructure as Code Ready

---

# 🏗 Architecture

```
IoT Devices
     │
     ▼
AWS IoT Core
     │
IoT Rule
     │
     ▼
AWS Lambda
(Data Validation & Processing)
     │
     ▼
Amazon S3 (Raw Data)
     │
     ▼
AWS Glue Crawler
     │
     ▼
AWS Glue ETL Job
     │
     ▼
Amazon S3 (Curated Parquet Data)
     │
     ▼
Amazon Athena
     │
     ▼
Amazon QuickSight
```

---

# 🖼 Architecture Diagram

Place your architecture image here.

```
docs/
 ├── architecture.png
 └── architecture.drawio
```

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Cloud Provider | AWS |
| Messaging | MQTT |
| Compute | AWS Lambda |
| Storage | Amazon S3 |
| ETL | AWS Glue |
| SQL Analytics | Amazon Athena |
| Visualization | Amazon QuickSight |
| Monitoring | Amazon CloudWatch |
| Identity | AWS IAM |

---

# 📂 Repository Structure

```
serverless-iot-lakehouse/

│
├── docs/
│   ├── architecture.drawio
│   ├── architecture.png
│   └── screenshots/
│
├── simulator/
│   ├── iot_simulator.py
│   └── config.py
│
├── lambda/
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── tests/
│
├── glue/
│   ├── crawler/
│   ├── etl_job.py
│   └── schema/
│
├── athena/
│   ├── create_tables.sql
│   ├── queries.sql
│   └── views.sql
│
├── dashboard/
│   └── quicksight/
│
├── infrastructure/
│   ├── terraform/
│   └── cloudformation/
│
├── api_tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

# ⚙ Workflow

### Step 1

IoT devices publish sensor data via MQTT.

↓

### Step 2

AWS IoT Core securely receives device messages.

↓

### Step 3

IoT Rules trigger AWS Lambda.

↓

### Step 4

Lambda validates, enriches and stores incoming data into Amazon S3.

↓

### Step 5

AWS Glue Crawlers automatically detect schemas.

↓

### Step 6

Glue ETL transforms raw JSON into optimized Parquet datasets.

↓

### Step 7

Athena performs serverless SQL analytics.

↓

### Step 8

QuickSight generates interactive dashboards.

---

# 📊 Example Sensor Data

```json
{
  "deviceId": "sensor-001",
  "temperature": 27.3,
  "humidity": 62,
  "pressure": 1014,
  "timestamp": "2026-07-03T09:30:00Z"
}
```

---

# 📈 Example Athena Query

```sql
SELECT
deviceid,
AVG(temperature) AS average_temperature
FROM iot_sensor_data
GROUP BY deviceid
ORDER BY average_temperature DESC;
```

---

# 📊 Dashboard Insights

The QuickSight dashboard provides:

- Average Temperature
- Average Humidity
- Sensor Health
- Device Activity
- Event Volume
- Hourly Trends
- Daily Trends
- Peak Usage
- Device Distribution
- Sensor Status

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/yourusername/serverless-iot-lakehouse.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure AWS CLI

```bash
aws configure
```

---

## Deploy Infrastructure

Terraform

```bash
terraform init
terraform apply
```

or

CloudFormation

```bash
aws cloudformation deploy
```

---

# 📸 Project Screenshots

```
docs/screenshots/

├── architecture.png
├── lambda_logs.png
├── glue_crawler.png
├── glue_job.png
├── athena_query.png
├── quicksight_dashboard.png
├── cloudwatch_logs.png
├── s3_bucket.png
└── iot_core.png
```

---

# 📊 Performance

| Metric | Value |
|---------|-------|
| Architecture | Serverless |
| Average Lambda Runtime | ~120 ms |
| Query Engine | Amazon Athena |
| Data Format | Parquet |
| ETL Engine | AWS Glue |
| Scalability | Automatic |
| Availability | High |
| Infrastructure Management | None |

---

# 🔒 Security

- IAM Least Privilege
- Encryption at Rest
- Encryption in Transit
- Secure MQTT Communication
- CloudWatch Logging
- AWS Managed Services
- Data Validation
- Error Handling
- Retry Mechanism

---

# 🌟 Future Improvements

- Amazon Kinesis Integration
- Real-Time Stream Analytics
- AWS Step Functions
- SNS Alerts
- EventBridge Automation
- ML-based Anomaly Detection
- Predictive Maintenance
- Grafana Dashboards
- Multi-region Deployment
- Device Digital Twin

---

# 📚 AWS Services Used

- AWS IoT Core
- AWS Lambda
- Amazon S3
- AWS Glue
- AWS Glue Crawlers
- Amazon Athena
- Amazon QuickSight
- AWS IAM
- Amazon CloudWatch

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Designing serverless cloud architectures
- Building scalable IoT pipelines
- Event-driven computing
- Data lake architecture
- ETL pipelines
- SQL analytics on large datasets
- Cloud security best practices
- Infrastructure as Code
- Cost optimization in AWS

---

# 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Haneef Ahmad**

- LinkedIn: www.linkedin.com/in/haneefahmad2004
- GitHub: https://github.com/haneefahmad

---

## ⭐ If you found this project useful, please consider giving it a star!
