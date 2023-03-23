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


## Endpoint API using CURL

### 1. Call Endpoint for Inference 

Adds an inference call to the queue

Returns inference results if available in <10 seconds, else returns a Call ID

#### API VERSION 1
```
https://api.banana.dev/start/v4
```
method : POST

example -
```
curl -X POST https://api.runpod.ai/v1/<API_ID>/run \
-H 'Content-Type: application/json'                             \
-H 'Authorization: Bearer <API TOKEN>'    \
-d '{"input": {"contentt": "a cute magical flying dog, fantasy art drawn by disney concept artists"}}'
```
sample ouput in json:
```
{
    "id": "<job_ID>",
    "status": "IN_QUEUE"
}
```

curl command to check status:
```
curl https://api.runpod.ai/v1/<API_ID>/status/<job_ID> \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
```
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

```

## MODEL INPUTS from wikis
```
{
    'input':
            {
                {
                    'content": "Tron is a decentralized, blockchain-based, open-source protocol supporting various kinds of blockchain networks and smart contract systems including bitcoin, Ethereum, EOS, Qtum, and other public blockchain smart contracts TRON features a delegated proof-of-stake(DPoS) principles as its consensus algorithm and a cryptocurrency native to the system, known as Tronix (TRX). Tron was established in March 2014 by Justin Sun and since 2017 it has been overseen and supervised by the a non-profit 'TRON Foundation' organization in Singapore which was established in the same year. TRX is the mainnet native token of the TRON protocol issued by TRON DAO which is a community-governed DAO dedicated to accelerating the decentralization of the internet blockchain technology and DApps. TRX is the basic unit of accounts on the TRON blockchain. TRX is also a natural medium currency for all TRC-based tokens. TRX connects the whole TRON ecosystem with abundant application scenarios that power transactions and applications on the chain. TRX was originally an Ethereum-based ERC-20 token, but switched its protocol to its own blockchain in 2018. TRC20 has a fee of 5 Tron per 1 USDT coin for the transfer. Overview History 2017 The TRON Foundation was established in July 2017 in Singapore. TRON was founded by Justin Sun in September 2017. The Foundation raised $70 million in 2017 through an initial coin offering before China outlawed the digital tokens. 2018 The blockchain Explorer 'testnet', and Web Wallet were all launched in March 2018. TRON Mainnet launched shortly afterward in May 2018 marking the Odyssey 2.0 release as a key technical milestone for TRON. In June 2018, TRON switched its protocol from an ERC-20 token on top of Ethereum to an independent peer-to-peer network. In July 2018, the TRON Foundation announced it had finished the acquisition of BitTorrent, a peer-to-peer file-sharing service. With this, TRON declared its independence with the creation of the Genesis block.",

                }
            }
            
}
```

## OUTPUT
```
{
    "delayTime":45,
    "executionTime":3861,
    "id":"0690154d-de51-4455-86af-290f6ec7c964",
    "input":{
                "content":"Tron is a decentralized, blockchain-based, open-source protocol supporting various kinds of blockchain networks and smart contract systems including bitcoin, Ethereum, EOS, Qtum, and other public blockchain smart contracts TRON features a delegated proof-of-stake(DPoS) principles as its consensus algorithm and a cryptocurrency native to the system, known as Tronix (TRX). Tron was established in March 2014 by Justin Sun and since 2017 it has been overseen and supervised by the a non-profit \'TRON Foundation\' organization in Singapore which was established in the same year. TRX is the mainnet native token of the TRON protocol issued by TRON DAO which is a community-governed DAO dedicated to accelerating the decentralization of the internet blockchain technology and DApps. TRX is the basic unit of accounts on the TRON blockchain. TRX is also a natural medium currency for all TRC-based tokens. TRX connects the whole TRON ecosystem with abundant application scenarios that power transactions and applications on the chain. TRX was originally an Ethereum-based ERC-20 token, but switched its protocol to its own blockchain in 2018. TRC20 has a fee of 5 Tron per 1 USDT coin for the transfer. Overview History 2017 The TRON Foundation was established in July 2017 in Singapore. TRON was founded by Justin Sun in September 2017. The Foundation raised $70 million in 2017 through an initial coin offering before China outlawed the digital tokens. 2018 The blockchain Explorer \'testnet\', and Web Wallet were all launched in March 2018. TRON Mainnet launched shortly afterward in May 2018 marking the Odyssey 2.0 release as a key technical milestone for TRON. In June 2018, TRON switched its protocol from an ERC-20 token on top of Ethereum to an independent peer-to-peer network. In July 2018, the TRON Foundation announced it had finished the acquisition of BitTorrent, a peer-to-peer file-sharing service. With this, TRON declared its independence with the creation of the Genesis block."
        },
        
   "output":
   [
        {
            "summary_text":"Tron is a decentralized, open-source protocol supporting various kinds of blockchain networks and smart contract systems ."
        }
    ],
    
    "status":"COMPLETED"
}
```

## Usefull links
Runpod API Docs : [https://docs.banana.dev/banana-docs/](https://docs.runpod.io/ai-endpoints/runpod-apis)]([https://docs.banana.dev/banana-docs/](https://docs.runpod.io/ai-endpoints/runpod-apis)

Runpod Custom API's template : [https://app.banana.dev/templates/EveripediaNetwork/summary-banana-template](https://docs.runpod.io/serverless-gpus/custom-apis)

Create Your own Container:
[https://docs.runpod.io/serverless-gpus/custom-apis](https://docs.runpod.io/serverless-gpus/custom-apis/worker-image-creation)

Hugging face repository : [https://huggingface.co/braindao/flan-t5-cnn](https://huggingface.co/braindao/flan-t5-cnn)

<br>

<br>
