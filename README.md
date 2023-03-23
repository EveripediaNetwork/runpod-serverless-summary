# BrainDAO's Package for deploying fine tuned flan-T5 on Runpod

## This repo helps you with the following: 
     
   - [Using our inference Endpoint](#1)
   - [Cloing our container on your machine](#2)
   - [Deploying our container in your runpod account](#3)
   - [Details about the fine tuned model](#4)

<a name='1'></a>
### 1. Call our Endpoint for Inference 

Adds an inference call to the queue

#### API VERSION 2

[https://api.banana.dev/start/v2/](https://api.runpod.ai/v2/)

method : POST

#### Using cURL
- example
```
curl -X POST https://api.runpod.ai/v2/5oegxkas8q653w/runsync \
-H 'Content-Type: application/json'                             \
-H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'    \
-d '{"input": {
        "content": "Tron is a decentralized, blockchain-based, open-source protocol supporting various kinds of blockchain networks and smart contract systems including bitcoin, Ethereum, EOS, Qtum, and other public blockchain smart contracts TRON features a delegated proof-of-stake(DPoS) principles as its consensus algorithm and a cryptocurrency native to the system, known as Tronix (TRX). Tron was established in March 2014 by Justin Sun and since 2017 it has been overseen and supervised by the a non-profit TRON Foundation organization in Singapore which was established in the same year. TRX is the mainnet native token of the TRON protocol issued by TRON DAO which is a community-governed DAO dedicated to accelerating the decentralization of the internet blockchain technology and DApps. TRX is the basic unit of accounts on the TRON blockchain. TRX is also a natural medium currency for all TRC-based tokens. TRX connects the whole TRON ecosystem with abundant application scenarios that power transactions and applications on the chain. TRX was originally an Ethereum-based ERC-20 token, but switched its protocol to its own blockchain in 2018. TRC20 has a fee of 5 Tron per 1 USDT coin for the transfer. Overview History 2017 The TRON Foundation was established in July 2017 in Singapore. TRON was founded by Justin Sun in September 2017. The Foundation raised $70 million in 2017 through an initial coin offering before China outlawed the digital tokens. 2018 The blockchain Explorer testnet, and Web Wallet were all launched in March 2018. "  
}}'
```
sample ouput in json:
```
{
    "id": "782c0db8-271a-424f-8bc6-a6e66582f1b7",
    "status": "IN_QUEUE"
    [{'summary_text': 'Tron is a decentralized, open-source protocol supporting various kinds of blockchain networks and smart contract systems .'}]
}
```


#### Using Python
- example
```
import runpod

runpod.api_key = "YOUR_API_KEY"
endpoint = runpod.Endpoint("ENDPOINT_ID")

run_request = endpoint.run(
    {"YOUR_MODEL_INPUT_JSON": "YOUR_MODEL_INPUT_VALUE"}
)

# Check the status of the endpoint run request
print(run_request.status())

# Get the output of the endpoint run request, blocking until the endpoint run is complete.
print(run_request.output())
```

#### Using NodeJS
- example
```
const request = require('request');

// Set the API endpoint and model name
const endpoint = 'https://api.runpod.ai/v2/5oegxkas8q653w/runsync';

// Set the API key and input data
const apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
const inputData = {
  input: {
    prompt: 'My creative vision.',
  },
};

// Set the headers for the request
const headers = {
  'Content-Type': 'application/json',
  Authorization: `Bearer ${apiKey}`,
};

// Make the request
request.post(
  {
    url: endpoint,
    json: inputData,
    headers,
  },
  (err, response) => {
    if (err) {
      console.error(err);
      return;
    }

    // Print the response
    console.log(response.body);
  },
);
```
#### Using Go
- example
```
package main

import (
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "log"
  "net/http"
)

func main() {
  // Set the API endpoint and model name
  endpoint := "https://api.runpod.ai/v2/5oegxkas8q653w/runsync" 

  // Set the API key and input data
  apiKey := "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  inputData := map[string]interface{}{
    "input": map[string]string{
      "prompt": "My creative vision.",
    },
  }

  // Convert the input data to JSON
  inputJSON, err := json.Marshal(inputData)
  if err != nil {
    log.Fatal(err)
  }

  // Set the headers for the request
  headers := map[string][]string{
    "Content-Type": {"application/json"},
    "Authorization": {fmt.Sprintf("Bearer %s", apiKey)},
  }

  // Make the request
  resp, err := http.Post(endpoint, "application/json", bytes.NewBuffer(inputJSON))
  if err != nil {
    log.Fatal(err)
  }
  defer resp.Body.Close()

  // Print the response
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(string(body))
}
```

<a name='2'></a>
## 2. To run our model on your'r local Machine:

1. Load the serverless template into your local machine

```
git clone https://github.com/EveripediaNetwork/runpod-serverless-summary.git
```
2. now intall packages required

```
pip3 install -r requirements.txt
```

3. To run & test the handler in terminal 

```
python3 app.py
```
The above commands invokes app.py file for running on python env, takes test_input.json file in the directory as input and generates result on your terminal.

<a name='3'></a>
## 3. Deploying our Model on you'r Runpod:

1. Create an account on Runpod [Sign up for Runpod](https://www.runpod.io/)

2. Goto Templates on runpod [Runpod Serverless Templates](https://www.runpod.io/console/serverless/user/templates)

3. Select New Template 
![Fill data in Template & Save](https://github.com/EveripediaNetwork/runpod-serverless-summary/blob/main/images/new_template.png?raw=true)
2. Give Your Template a Name ( optional )
3. Paste ``` ghcr.io/everipedianetwork/runpod-serverless-summary:latest ``` in container image section
4. Keep your Container disk space atleast 15GB allocated
5. Save the Template
![New Template](https://github.com/EveripediaNetwork/runpod-serverless-summary/blob/main/images/template.png?raw=true)

### 3. Creating API endpoint 
Go to Runpod API dashbooard 
[Runpod API dashboard](https://www.runpod.io/console/serverless/user/apis)

1. Select New API
![New API](https://github.com/EveripediaNetwork/runpod-serverless-summary/blob/main/images/api_details.png?raw=true)
2. Create an API by entering:
* name of api
* template to use on the api 
* Min & Max Workers (these values varies as per the need & Requirement)
* Select the available GPUs
* Click Update
![Save API](https://github.com/EveripediaNetwork/runpod-serverless-summary/blob/main/images/save_api.png?raw=true)

<a name='4'></a>
## 4. Details about the Model We are Using:
```
## Training and evaluation data
* Loss: 1.4232

* Rouge1: 42.1388

* Rouge2: 19.7696

* Rougel: 30.1512

* Rougelsum: 39.3222

* Gen Len: 71.8562

## Training hyperparameters

The following hyperparameters were used during training:

* learning_rate: 0.0001

* train_batch_size: 1

* eval_batch_size: 4

* seed: 42

* gradient_accumulation_steps: 64

* total_train_batch_size: 64

* optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08

* lr_scheduler_type: Constant

* num_epochs: 3.0

## Framework versions

Transformers 4.27.0.dev0

Pytorch 1.13.0+cu117

Datasets 2.7.1

Tokenizers 0.12.1

```

## Usefull links
Runpod API Docs : [https://docs.banana.dev/banana-docs/](https://docs.runpod.io/ai-endpoints/runpod-apis)

Runpod Custom API's template : [https://app.banana.dev/templates/EveripediaNetwork/summary-banana-template](https://docs.runpod.io/serverless-gpus/custom-apis)

Create Your own Container:
[https://docs.runpod.io/serverless-gpus/custom-apis](https://docs.runpod.io/serverless-gpus/custom-apis/worker-image-creation)

Hugging face repository : [https://huggingface.co/braindao/flan-t5-cnn](https://huggingface.co/braindao/flan-t5-cnn)

<br>

<br>
