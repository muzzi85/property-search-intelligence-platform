import azure.functions as func
import json
from openai import AzureOpenAI
import os

# Configure Azure OpenAI client
# client = AzureOpenAI(
#     api_version="2024-12-01-preview",
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.getenv("AZURE_OPENAI_API_KEY")
# )


def extract_property_info(sentence: str, client):
    prompt = f"""
    You are a real estate and data extraction expert. Extract structured JSON information from the user's sentence
    about a property search. Include:

    1. The extracted value for each key (based on the description below).
    2. A confidence score between 0 and 1 for each key.
    3. A reasoning explanation for each key.

    Keys and expected value types:
    1. bedrooms → integer (number of bedrooms)
    2. location → string (area, city, or neighbourhood)
    3. min_price → integer (lowest mentioned price or budget)
    4. max_price → integer (highest mentioned price or budget)
    5. price_period → string ("month", "week", "year" or "unspecified")
    6. type → string ("flat", "house", "studio", "bungalow", etc.)
    7. deal → string ("rent" or "sale")
    8. furnishing → string ("furnished", "unfurnished", "part-furnished", or "unspecified")
    9. garden → string ("yes" or "no")
    10. parking → string ("Street parking", "Private parking", "Driveway", "Garage", or "unspecified")
    11. security → string ("high", "medium", "low", or "unspecified")
    12. noise_preference → string ("quiet", "lively", or "unspecified")
    13. crime_preference → string ("low", "medium", "unspecified")
    14. school_quality → integer (0 to 5, where 5 = best Ofsted rating)
    15. EPC_rating → string ("A", "B", "C", "D", "E", "F", "G")
    16. pet_friendly → string ("yes" or "no")
    17. EV_charging → string ("yes" or "no")
    18. high_ceilings → string ("yes" or "no")
    19. available_from → string ("last 24 hours", "last 3 days", "last week", "last 14 days", or "unspecified")
    20. near_community → list of strings (names of nearby community places or amenities mentioned)

    Possible values for near_community include:
    [
    "school", "nursery", "college", "library",
    "bus_stop", "train_station", "tram_stop", "airport",
    "gym", "park", "sports_centre", "swimming_pool",
    "restaurant", "cafe", "pub", "shopping_centre", "market",
    "hospital", "pharmacy", "clinic", "police_station",
    "supermarket", "post_office", "bank",
    "community_centre", "church", "mosque", "temple",
    "co_working_space", "dog_park", "vet_clinic"
    ]

    Return JSON only in the following format:

    {{
    "bedrooms": ...,
    "bedrooms_confidence": ...,
    "location": ...,
    "location_confidence": ...,
    ...
    "reasoning": {{
        "bedrooms": "...",
        "location": "...",
        ...
    }}
    }}
    User sentence:
    \"\"\"{sentence}\"\"\"
    """


    response = client.chat.completions.create(
        model="gpt-4o",  # Use gpt-4o-mini for cost-effective real-time inference
        messages=[
            {"role": "system", "content": "You are a precise property information extractor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    output_text = response.choices[0].message.content
    try:
        start = output_text.find("{")
        end = output_text.rfind("}") + 1
        return json.loads(output_text[start:end])
    except Exception:
        return {"error": "Failed to parse JSON", "raw_output": output_text}

def get_client():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not endpoint or not api_key:
        raise ValueError("Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_API_KEY")

    return AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=endpoint,
        api_key=api_key
    )


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        sentence = body.get("sentence", "")

        # Initialize client at runtime
        client = get_client()

        result = extract_property_info(sentence, client)
        return func.HttpResponse(json.dumps(result), mimetype="application/json", status_code=200)

    except ValueError as ve:
        return func.HttpResponse(
            json.dumps({"error": str(ve)}),
            mimetype="application/json",
            status_code=500
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
