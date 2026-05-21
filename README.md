
# 🏠 Azure Property Intelligence API

A cloud-native NLP API for extracting structured real-estate search intelligence using Azure Functions and Python.

The platform converts unstructured property search text into structured JSON metadata for downstream analytics, filtering, and recommendation systems.

Built using:

`Python • Azure Functions • REST APIs • NLP • Azure Cloud`

---

# 🚀 Business Problem

Real-estate platforms receive thousands of unstructured user search queries such as:

```text
Looking for a 2-bedroom flat in Manchester for rent, max 1200 per month
```

These queries contain valuable structured information:
- location
- property type
- bedroom count
- rental intent
- price constraints

However, most systems receive them as plain text.

This project automates extraction of structured search intelligence for:
- property platforms
- recommendation engines
- search optimization
- analytics systems
- customer intent modelling

---

# 💡 What This API Does

The API extracts:

✅ city/location  
✅ property type  
✅ bedroom count  
✅ rent/sale intent  
✅ pricing constraints  
✅ search preferences  

and converts them into structured machine-readable JSON.

---

# 📊 Example Input

```json
{
  "sentence": "Looking for a 2-bedroom flat in Manchester for rent, max 1200 per month."
}
```

---

# 📊 Example Output

```json
{
  "location": "Manchester",
  "property_type": "flat",
  "bedrooms": 2,
  "transaction_type": "rent",
  "max_price": 1200
}
```

---

# 🧠 NLP Processing Workflow

```text
User Query
     ↓
Azure Function API
     ↓
NLP Extraction Engine
     ↓
Entity Detection
     ↓
Structured Property Metadata
     ↓
JSON Response
```

---

# ☁️ Cloud Architecture

The platform is deployed using Azure cloud-native services.

Architecture components include:

- Azure Functions
- Python runtime
- HTTP-triggered APIs
- REST endpoints
- JSON response pipelines

---

# ⚡ Technical Features

## NLP Features

- keyword extraction
- entity parsing
- structured metadata extraction
- property intent detection
- pricing extraction

## Cloud Features

- serverless deployment
- Azure Functions
- REST API architecture
- scalable cloud endpoints
- lightweight inference pipeline

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Language | Python |
| Cloud Platform | Microsoft Azure |
| Compute | Azure Functions |
| API | REST |
| Domain | NLP / Real Estate Intelligence |

---

# 📈 Potential Use Cases

This platform can support:

- PropTech applications
- property search systems
- recommendation engines
- customer intent analytics
- chatbot integrations
- intelligent search platforms
- listing optimization systems

---

# 🔮 Future Improvements

Potential future enhancements include:

- LLM-based extraction
- semantic search
- multilingual support
- GraphRAG integration
- vector search
- recommendation systems
- real-time analytics pipelines

---

# ⚠️ Copyright & License

Copyright © 2026 Mustafa Alhamdi. All rights reserved.

This repository and its contents are provided for educational, research, and portfolio purposes only.

Unauthorized copying, redistribution, commercial usage, or reproduction of this codebase without explicit permission is prohibited.

---

# 👨‍💻 Author

Built as an applied NLP and cloud engineering project exploring:

- cloud-native AI systems
- Azure serverless architecture
- information extraction
- search intelligence
- real-estate NLP
- scalable API engineering

curl -v -X POST "https://my-property-extractor.azurewebsites.net/api/extract_property?code=dDp34vmiK0mn4qBq2yWkkz2rM1cLO9IMkLyPyGfQzLwEAzFu9-tJqQ==" -H "Content-Type: application/json" -d '{"sentence":"Looking for a 2-bedroom flat in Manchester for rent, max 1200 per month."}'


curs -v -X POST "https://my-property-extractor.azurewebsites.net/api/extract_property?code=dDp34vmiK0mn4qBq2yWkkz2rM1cLO9IMkLyPyGfQzLwEAzFu9-tJqQ==" -H
 "Content-Type: application/json" -d '{"sentence":"Looking for a 2-bedroom flat in Manchester for rent, max 1200 per month. -o output.json

 az functionapp create     --resource-group searchai     --consumption-plan-location eastus     --runtime python     --functions-version 4     --name my-property-extractor     --storage-account uisearchengine2025xyz     --os-type Linux     --runtime-version 3.10

 func azure functionapp publish my-property-extractor

  az functionapp cors add     --name my-property-extractor     --resource-group searchai     --allowed-origins https://portal.azure.com

  az storage account show --name uisearchengine2025xyz --resource-group searchai

  az storage account create     --name uisearchengine2025xyz     --resource-group searchai     --location eastus     --sku Standard_LRS     --kind StorageV2     --subscription b2dc8e41-a4c4-4f97-a443-7446dfe9dce2

az account show

az login --use-device-code

   az account set --subscription b2dc8e41-a4c4-4f97-a443-7446dfe9dce2

   az account list --output table

   
