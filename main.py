from flask import Flask, request, jsonify
from pydantic import BaseModel
import openai
import base64
import os

app = Flask(__name__)

class AnalysisRequest(BaseModel):
    api_key: str
    image: str

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        request_data = AnalysisRequest(**data)

        openai.api_key = request_data.api_key  # ✅ Correct way to set the key

        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert AI radiologist analyzing medical images. "
                            "Provide a detailed diagnosis and highlight any abnormalities."
                        )
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    "Please analyze this chest X-ray image for any signs of disease, consolidation, or abnormality."
                                )
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{request_data.image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=2000,
                temperature=0.2
            )

            analysis = response.choices[0].message.content

            references_response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Provide relevant medical literature references or PubMed articles that support the above analysis."
                        )
                    },
                    {
                        "role": "user",
                        "content": analysis
                    }
                ],
                max_tokens=1000,
                temperature=0.2
            )

            references = references_response.choices[0].message.content

            return jsonify({"analysis": analysis, "references": references})

        except openai.OpenAIError as e:
            return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"Request processing error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
