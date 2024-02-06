# mixtral.py
A versatile Python module for running the Mixtral language model with customisable precision and attention mechanisms.

## Installation
```
pip/pip3 install mixtral.py
```

## Usage
### Run the model
```python
import mixtral
mixtral = Mixtral(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
print("Running the model:")
print(mixtral.generate_text("Hello my name is"))
```
### In half-precision
```python
import mixtral
print("Running the model in half precision:")
mixtral_half_precision = Mixtral(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1", use_half_precision=True)
print(mixtral_half_precision.generate_text("Hello my name is"))
```
### Lower precision using (8-bit & 4-bit) using `bitsandbytes`
```python
import mixtral
print("Running the model in lower precision using (8-bit & 4-bit) using bitsandbytes:")
mixtral_4bit = Mixtral(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1", load_in_4bit=True)
print(mixtral_4bit.generate_text("Hello my name is"))
```
### Load the model with Flash Attention 2
```python
import mixtral
print("Load the model with Flash Attention 2:")
mixtral_flash_attention_2 = Mixtral(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1", use_flash_attention_2=True)
print(mixtral_flash_attention_2.generate_text("Hello my name is"))
```
# Limitations
The Mixtral-8x7B Instruct model showcases the ease of fine-tuning the base model for impressive performance, lacking moderation mechanisms. Mixtral-8x7B seek community input on implementing guardrails for deployment in environments needing moderated outputs.
