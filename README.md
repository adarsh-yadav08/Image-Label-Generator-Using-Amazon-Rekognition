# 🖼️ Image Labels Generator using Amazon Rekognition

This project is a **serverless image label detection system** built using **AWS Rekognition**, **AWS Lambda**, and **Amazon S3**. It automatically detects objects, scenes, and concepts in images uploaded to an S3 bucket and returns labels with confidence scores.

It’s ideal for learning cloud automation and serverless architecture, and perfect to showcase on your GitHub and resume.

---

## 📌 Features

- 🧠 Uses **Amazon Rekognition** to analyze images
- ☁️ Triggered automatically when a new image is uploaded to **Amazon S3**
- ⚙️ Runs a **Lambda function** to process the image and extract labels
- 📝 Logs results in **CloudWatch**
- 💡 Easily extendable to store data or integrate with frontends

---

## 🛠️ Tech Stack

| Component         | Usage                                   |
|------------------|-----------------------------------------|
| **Amazon S3**     | Store uploaded images                   |
| **Amazon Rekognition** | Analyze image content (labels)     |
| **AWS Lambda**     | Serverless function to run detection   |
| **IAM Roles**      | Manage access and permissions          |
| **CloudWatch**     | Logs detection results                 |
| **Python**         | Lambda function written in Python      |

---

## 🗂️ Project Structure

image-labels-generator/ ├── lambda_function/ │ ├── handler.py # Lambda function code │ └── requirements.txt # Dependencies (if deploying externally) ├── docs/ │ ├── architecture.png # System architecture diagram (add image) │ └── example_output.json # Sample output labels from Rekognition ├── README.md # Project documentation └── .gitignore # Ignore unnecessary files


---

## 🔧 How It Works

1. You upload an image (JPG/PNG) to an **S3 bucket**.
2. The upload triggers an **AWS Lambda** function.
3. The function uses the **Rekognition API** to detect labels in the image.
4. Results (like `"Dog"` or `"Car"`) are returned as JSON and printed to **CloudWatch Logs**.

---

## 🔨 How to Deploy (Step-by-Step)

### 1. Set Up Your AWS Environment
- Sign in to your [AWS account](https://aws.amazon.com/console/).
- Install and configure the AWS CLI (`aws configure`) if needed.

### 2. Create an S3 Bucket
- Go to **Amazon S3 → Create bucket**
- Name it something unique (e.g., `image-labels-demo-bucket`)
- Region: Select the same region you’ll use for Lambda

### 3. Create an IAM Role
- Go to **IAM → Roles → Create role**
- Choose **Lambda** as the trusted entity
- Attach the following policies:
  - `AmazonS3ReadOnlyAccess`
  - `AmazonRekognitionFullAccess`
  - `CloudWatchLogsFullAccess`
- Name it `LambdaRekognitionRole`

### 4. Create the Lambda Function
- Go to **Lambda → Create function**
- Name it `ImageLabelsFunction`
- Runtime: `Python 3.9`
- Choose existing role: `LambdaRekognitionRole`
- In the function editor, paste the contents of `lambda_function/handler.py`

### 5. Add an S3 Trigger
- In your Lambda function, click **Add Trigger**
- Select **S3**, choose your bucket
- Event type: `PUT` (object create)
- Check “Add permissions to allow S3 to invoke function”

### 6. Upload an Image to Test
- Go to your S3 bucket → Upload an image (e.g., `dog.jpg`)
- Open **CloudWatch Logs** → Find your Lambda log group → View logs
- You should see a list of labels like:

```json
[
  {
    "Name": "Dog",
    "Confidence": 98.45
  },
  {
    "Name": "Pet",
    "Confidence": 94.78
  }
]

