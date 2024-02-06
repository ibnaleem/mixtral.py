# mixtral.py
A Python module for running the [Mixtral-8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) language model with customisable precision and attention mechanisms. [Mixtral-8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1), being a pretrained base model, lacks moderation mechanisms. [Read more here.](https://mistral.ai/news/mixtral-of-experts/)

## Installation
```
pip/pip3 install mixtral.py
```

## Usage
### Run the model
```python
import mixtral
mixtral = Mixtral()
print("Running the model:")
print(mixtral.generate_text("..."))
```
### In half-precision
```python
import mixtral
print("Running the model in half precision:")
mixtral_half_precision = Mixtral(use_half_precision=True)
print(mixtral_half_precision.generate_text("..."))
```
### Lower precision using (8-bit & 4-bit) using `bitsandbytes`
```python
import mixtral
print("Running the model in lower precision using (8-bit & 4-bit) using bitsandbytes:")
mixtral_4bit = Mixtral(load_in_4bit=True)
print(mixtral_4bit.generate_text("..."))
```
### Load the model with Flash Attention 2
```python
import mixtral
print("Load the model with Flash Attention 2:")
mixtral_flash_attention_2 = Mixtral(use_flash_attention_2=True)
print(mixtral_flash_attention_2.generate_text("..."))
```
## Hardware Requirements
- minimum 100GB GPU RAM ([Mistral AI](https://docs.mistral.ai/models/))
- Hardware requirements after fine-tuning can be found in the discussion [here](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1/discussions/3)
## Licenses
- mixtral.py is under the [GNU General Public License v3](https://github.com/ibnaleem/mixtral.py/blob/main/LICENSE)
- Mixtral 8x7b is under the [Apache 2.0 License](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)
## Contributing
I welcome contributions from the community and appreciate the time and effort put into making [mixtral.py](https://github.com/ibnaleem/mixtral.py) better. To contribute, please follow the guidelines and steps outlined below:

> Note: **_Your pull request will be closed if you do not specify the changes you've made._**

### Fork the Repository
Start by [forking this repository](https://github.com/ibnaleem/mixtral.py/fork). You can do this by clicking on the ["Fork"](https://github.com/ibnaleem/mixtral.py/fork) button located at the top right corner of the GitHub page. This will create a personal copy of the repository under your own GitHub account.

### Clone the Repository
Next, clone the forked repository to your local machine using the following command:
```bash
$ git clone https://github.com/yourusername/mixtral.py.git
```
Navigate to the cloned directory:
```bash 
$ cd mixtral.py
```
### Create a New Branch
Before making any changes, it's recommended to create a new branch. This ensures that your changes won't interfere with other contributions and keeps the main branch clean. Use the following command to create and switch to a new branch:
```bash
$ git checkout -b branch-name
```
### Make the Desired Changes
Now, you can proceed to make your desired changes to the project. Whether it's fixing bugs, adding new features, improving documentation, or optimizing code, your efforts will be instrumental in enhancing the project.

### Commit and Push Changes
Once you have made the necessary changes, commit your work using the following commands:
```bash
$ git add .
$ git commit -m "Your commit message"
```
Push the changes to your forked repository:
```bash
$ git push origin branch-name
```
### Submit a Pull Request
Head over to the [original repository](https://github.com/ibnaleem/mixtral.py) on GitHub and go to the ["Pull requests"](https://github.com/ibnaleem/mixtral/pulls) tab.
1. Click on the "New pull request" button.
2. Select your forked repository and the branch containing your changes.
3. Provide a clear and informative title for your pull request, and use the description box to explain the modifications you have made. **_Your pull request will be closed if you do not specify the changes you've made._**
4. Finally, click on the "Create pull request" button to submit your changes.

## Verifying Signatures
### Import PGP Key into Keyring
```
gpg --keyserver 185.125.188.27 --recv-keys 20247EC023F2769E66181C0F581B4A2A862BBADE
```
or
```
wget https://github.com/ibnaleem/ibnaleem/blob/main/public_key.asc
```
### Download Signature
The signatures (.asc and .sig) can be found in the [/sig directory.](https://github.com/ibnaleem/mixtral.py/tree/main/sig) Download either of them. Open [an issue](https://github.com/ibnaleem/mixtral.py/issues) with the title "invalid signature/wrong signature/corrupt signature" for any issues regarding my signatures.
### Sign My Key 
```
gpg --sign-key 20247EC023F2769E66181C0F581B4A2A862BBADE
gpg --send-keys 20247EC023F2769E66181C0F581B4A2A862BBADE
```
If you cannot upload your signature, see ["*gpg: keyserver receive failed: No route to host*"](https://stackoverflow.com/questions/54801274/gpg-keyserver-receive-failed-no-route-to-host-stack-overflow)
### Verify
```
gpg --verify mixtral.py.asc mixtral.py
```
Desired output:
```
gpg: Signature made Tue  6 Feb 10:27:34 2024 GMT
gpg:                using RSA key 20247EC023F2769E66181C0F581B4A2A862BBADE
gpg: Good signature from "Ibn Aleem <ibnaleem@outlook.com>" [ultimate]
```
## Acknowledgements
- [PyTorch](https://pytorch.org)
- [Transformers library](https://pypi.org/project/transformers/)
- [mistralai/Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)
