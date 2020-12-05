from google.cloud import automl
from flask import Flask, render_template, request

# TODO(developer): Uncomment and set the following variables
project_id = "msds-434-fp"
model_id = "TCN7453890590879514624"

prediction_client = automl.PredictionServiceClient()

model_full_id = automl.AutoMlClient.model_path(
    project_id, "us-central1", model_id
)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        predictions = request.form
        for key, item in predictions.items():
            # extract string message
            sms = item

        text_snippet = automl.TextSnippet(
            content=sms, mime_type="text/plain"
        )
        payload = automl.ExamplePayload(text_snippet=text_snippet)
        response = prediction_client.predict(name=model_full_id, payload=payload)
        
        for annotation_payload in response.payload:
            pred = annotation_payload.display_name
            break

        return render_template('prediction.html', pred = pred, sms = sms)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080, debug = True)