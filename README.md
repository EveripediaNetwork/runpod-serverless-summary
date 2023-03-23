# BrainDAO's Package for deploying fine tuned flan-T5 on Runpod

## This repo holds the serverless template of Rupod to deploy Flan-T5 base model fine-tuned on CNN Daily Mail dataset for Summarisation.

## Getting started

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

## Model deployment in banana dev
### 1. Create an account on Runpod [Sign up for Runpod](https://www.runpod.io/)

### 2. Goto Templates on runpod [Runpod Serverless Templates](https://www.runpod.io/console/serverless/user/templates)

1. Select New Template
2. Give Your Template a Name ( optional )
3. Paste ghcr.io/everipedianetwork/runpod-serverless-summary:latest in container image section
4. Keep your disk space atleast 15GB allocated
5. Save the Template
![New Template](https://github.com/[EveripediaNetwork]/[
runpod-serverless-summary]/blob/[main]/images/template.png?raw=true)
![Fill data in Template & Save](https://github.com/[EveripediaNetwork]/[
runpod-serverless-summary]/blob/[main]/images/new\ template.png?raw=true)

### 3. Creating API endpoint 
[Runpod API dashboard](https://www.runpod.io/console/serverless/user/apis)
Selectd New API

## Endpoint API using CURL
### 1. Start Endpoint
Adds an inference call to the queue

Returns inference results if available in <50 seconds, else returns a Call ID
#### API VERSION 4
```
https://api.banana.dev/start/v4
```
method : POST

example -
```
curl -X POST "https://api.banana.dev/start/v4/" \
-H "Content-Type: application/json" \
-d \
'
{
    "apiKey": "YOUR_API_KEY",
    "modelKey": "YOUR_MODEL_KEY",
    "modelInputs": {YOUR_MODEL_INPUT_JSON}
}'

```
full input json:
```
{

    "id": "xyz", // **optional -** some uuid to identify the payload
    "created": 123123123123, // **optional -** the current Unix timestamp in seconds
    "apiKey": "your-auth-key", // **required -** your api key, for authorization
    "modelKey": "your-model-key", // **required -** the key giving you access to this model
    "startOnly": false, // **optional -** boolean flag to tell backend to return a callID immediately, without awaiting results. Defaults to false.
    "modelInputs" : {
        ... // **required -** the json passed to the model inference server
    },
}
```
Calls to the Start endpoint, by default, remain on the server for one minute awaiting a result, to eliminate the need to run a subsequent Check call. This behavior can be toggled off with the "startOnly" flag.

return json:
```
{
    "id": "xyz" // the return payload id
    "message": "success", // success or server error messages. Our API does not throw 500 errors, so always check this field for the substring "error" to catch errors
    "created": 123123123123, // the current Unix timestamp in seconds
    "apiVersion": "Nov 14 2021", // identifier on which backend was used, to help us debug
    "callID": "call_abcabcabc", // the async call ID used on the /check/v4 call to see the task's status
    "finished": true, // a boolean to communicate that the inference is finished and you can expect values in the modelOutputs field
    "modelOutputs": [ {
        ... // the json returned from the model inference server
} ]
```
## 2. Check Endpoint
```
https://api.banana.dev/check/v4
```
method : POST

example-
```
curl -X POST "https://api.banana.dev/check/v4/" \
-H "Content-Type: application/json" \
-d \
'
{
    "apiKey": "YOUR_API_KEY",
    "callID": "TASK_ID_RETURNED_FROM_START_CALL"
}'
```
input json:
```
{
    "id": "xyz", // **optional -** some uuid to identify the payload
    "created": 123123123123, // **optional -** the current Unix timestamp in seconds
    "apiKey": "your-auth-key", // **required -** your api key, for authorization
    "longPoll": true, // **suggested -** a flag telling the REST call wait on the server for results, up to 50s
    "callID" : "call_abcabcabc" // **required -** the async task ID to fetch results for
}
```
return json:
```
{
    "id": "xyz" // the return payload id
    "message": "success", // success or server error messages. Our API does not throw 500 errors, so always check this field for the substring "error" to catch errors
    "created": 123123123123, // the current Unix timestamp in seconds
    "apiVersion": "Nov 14 2021", // identifier on which backend was used, to help us debug
    "modelOutputs": [ {
        ... // the json returned from the model inference server
    } ]
}
```
Because check is an async polling call, the status of the ongoing job will be displayed in the message field.

If ```message == "success"```,  then the results will be found in the modelOutputs field.

If ```message contains error```, then the inference failed.

Errors will not throw an api-wide 500 error, as the check call technically was successful.

Make sure to watch for errors in the message field.

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



## MODEL INPUTS from wikis
```
{
  'prompt': "Tron is a decentralized, blockchain-based, open-source protocol supporting various kinds of blockchain networks and smart contract systems including bitcoin, Ethereum, EOS, Qtum, and other public blockchain smart contracts TRON features a delegated proof-of-stake(DPoS) principles as its consensus algorithm and a cryptocurrency native to the system, known as Tronix (TRX). Tron was established in March 2014 by Justin Sun and since 2017 it has been overseen and supervised by the a non-profit 'TRON Foundation' organization in Singapore which was established in the same year. TRX is the mainnet native token of the TRON protocol issued by TRON DAO which is a community-governed DAO dedicated to accelerating the decentralization of the internet blockchain technology and DApps. TRX is the basic unit of accounts on the TRON blockchain. TRX is also a natural medium currency for all TRC-based tokens. TRX connects the whole TRON ecosystem with abundant application scenarios that power transactions and applications on the chain. TRX was originally an Ethereum-based ERC-20 token, but switched its protocol to its own blockchain in 2018. TRC20 has a fee of 5 Tron per 1 USDT coin for the transfer. Overview History 2017 The TRON Foundation was established in July 2017 in Singapore. TRON was founded by Justin Sun in September 2017. The Foundation raised $70 million in 2017 through an initial coin offering before China outlawed the digital tokens. 2018 The blockchain Explorer 'testnet', and Web Wallet were all launched in March 2018. TRON Mainnet launched shortly afterward in May 2018 marking the Odyssey 2.0 release as a key technical milestone for TRON. In June 2018, TRON switched its protocol from an ERC-20 token on top of Ethereum to an independent peer-to-peer network. In July 2018, the TRON Foundation announced it had finished the acquisition of BitTorrent, a peer-to-peer file-sharing service. With this, TRON declared its independence with the creation of the Genesis block.",
  'min_length' : 25, 
  'max_length' : 30
}

```

## OUTPUT
```
{'id': '178be9b8-6d12-4e9a-9c96-ea5d6f199a53',
 'message': 'success',
 'created': 1678436578,
 'apiVersion': 'January 11, 2023',
 'modelOutputs': [[{'summary_text': 'Tron is a decentralized, blockchain-based, open-source protocol supporting various kinds of blockchain networks and smart contract systems '}]]
 }
```

## Usefull links
Banana Docs : [https://docs.banana.dev/banana-docs/](https://docs.banana.dev/banana-docs/)

Model Template : [https://app.banana.dev/templates/EveripediaNetwork/summary-banana-template](https://app.banana.dev/templates/EveripediaNetwork/summary-banana-template)

Hugging face repository : [https://huggingface.co/braindao/flan-t5-cnn](https://huggingface.co/braindao/flan-t5-cnn)

<br>

<br>
