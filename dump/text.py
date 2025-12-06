

text = """
Parameters

config (T5Config) — Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
T5 model with a sequence classification/head on top (a linear layer on top of the pooled output) e.g. for GLUE tasks.

This model inherits from PreTrainedModel. Check the superclass documentation for the generic methods the library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads etc.)

This model is also a PyTorch torch.nn.Module subclass. Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage and behavior.

forward
<
source
>
( input_ids: typing.Optional[torch.LongTensor] = Noneattention_mask: typing.Optional[torch.Tensor] = Nonedecoder_input_ids: typing.Optional[torch.LongTensor] = Nonedecoder_attention_mask: typing.Optional[torch.LongTensor] = Noneencoder_outputs: typing.Optional[list[torch.FloatTensor]] = Noneinputs_embeds: typing.Optional[torch.FloatTensor] = Nonedecoder_inputs_embeds: typing.Optional[torch.FloatTensor] = Nonelabels: typing.Optional[torch.LongTensor] = Noneuse_cache: typing.Optional[bool] = Noneoutput_attentions: typing.Optional[bool] = Noneoutput_hidden_states: typing.Optional[bool] = Nonereturn_dict: typing.Optional[bool] = None ) → transformers.modeling_outputs.Seq2SeqSequenceClassifierOutput or tuple(torch.FloatTensor)

Expand 12 parameters
Parameters

input_ids (torch.LongTensor of shape (batch_size, sequence_length)) — Indices of input sequence tokens in the vocabulary. T5 is a model with relative position embeddings so you should be able to pad the inputs on both the right and the left.
Indices can be obtained using AutoTokenizer. See PreTrainedTokenizer.encode() and PreTrainedTokenizer.call() for detail.

What are input IDs?

To know more on how to prepare input_ids for pretraining take a look a T5 Training.

attention_mask (torch.Tensor of shape (batch_size, sequence_length), optional) — Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1]:
1 for tokens that are not masked,
0 for tokens that are masked.
What are attention masks?

decoder_input_ids (torch.LongTensor of shape (batch_size, target_sequence_length), optional) — Indices of decoder input sequence tokens in the vocabulary.
Indices can be obtained using AutoTokenizer. See PreTrainedTokenizer.encode() and PreTrainedTokenizer.call() for details.

What are decoder input IDs?

T5 uses the pad_token_id as the starting token for decoder_input_ids generation. If past_key_values is used, optionally only the last decoder_input_ids have to be input (see past_key_values).

To know more on how to prepare decoder_input_ids for pretraining take a look at T5 Training.

decoder_attention_mask (torch.BoolTensor of shape (batch_size, target_sequence_length), optional) — Default behavior: generate a tensor that ignores pad tokens in decoder_input_ids. Causal mask will also be used by default.
encoder_outputs (list[torch.FloatTensor], optional) — Tuple consists of (last_hidden_state, optional: hidden_states, optional: attentions) last_hidden_state of shape (batch_size, sequence_length, hidden_size), optional) is a sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention of the decoder.
inputs_embeds (torch.FloatTensor of shape (batch_size, sequence_length, hidden_size), optional) — Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert input_ids indices into associated vectors than the model’s internal embedding lookup matrix.
decoder_inputs_embeds (torch.FloatTensor of shape (batch_size, target_sequence_length, hidden_size), optional) — Optionally, instead of passing decoder_input_ids you can choose to directly pass an embedded representation. If past_key_values is used, optionally only the last decoder_inputs_embeds have to be input (see past_key_values). This is useful if you want more control over how to convert decoder_input_ids indices into associated vectors than the model’s internal embedding lookup matrix.
If decoder_input_ids and decoder_inputs_embeds are both unset, decoder_inputs_embeds takes the value of inputs_embeds.

labels (torch.LongTensor of shape (batch_size,), optional) — Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1]. If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
use_cache (bool, optional) — If set to True, past_key_values key value states are returned and can be used to speed up decoding (see past_key_values).
output_attentions (bool, optional) — Whether or not to return the attentions tensors of all attention layers. See attentions under returned tensors for more detail.
output_hidden_states (bool, optional) — Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for more detail.
return_dict (bool, optional) — Whether or not to return a ModelOutput instead of a plain tuple.
Returns

transformers.modeling_outputs.Seq2SeqSequenceClassifierOutput or tuple(torch.FloatTensor)

A transformers.modeling_outputs.Seq2SeqSequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False) comprising various elements depending on the configuration (T5Config) and inputs.

loss (torch.FloatTensor of shape (1,), optional, returned when label is provided) — Classification (or regression if config.num_labels==1) loss.

logits (torch.FloatTensor of shape (batch_size, config.num_labels)) — Classification (or regression if config.num_labels==1) scores (before SoftMax).

past_key_values (EncoderDecoderCache, optional, returned when use_cache=True is passed or when config.use_cache=True) — It is a EncoderDecoderCache instance. For more details, see our kv cache guide.

Contains pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.

decoder_hidden_states (tuple(torch.FloatTensor), optional, returned when output_hidden_states=True is passed or when config.output_hidden_states=True) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, + one for the output of each layer) of shape (batch_size, sequence_length, hidden_size).

Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.

decoder_attentions (tuple(torch.FloatTensor), optional, returned when output_attentions=True is passed or when config.output_attentions=True) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length).

Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the self-attention heads.

cross_attentions (tuple(torch.FloatTensor), optional, returned when output_attentions=True is passed or when config.output_attentions=True) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length).

Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the weighted average in the cross-attention heads.

encoder_last_hidden_state (torch.FloatTensor of shape (batch_size, sequence_length, hidden_size), optional) — Sequence of hidden-states at the output of the last layer of the encoder of the model.

encoder_hidden_states (tuple(torch.FloatTensor), optional, returned when output_hidden_states=True is passed or when config.output_hidden_states=True) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, + one for the output of each layer) of shape (batch_size, sequence_length, hidden_size).

Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.

encoder_attentions (tuple(torch.FloatTensor), optional, returned when output_attentions=True is passed or when config.output_attentions=True) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length).

Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the self-attention heads.


The T5ForSequenceClassification forward method, overrides the __call__ special method.

Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while the latter silently ignores them.

Example of single-label classification:

Copied
import torch
from transformers import AutoTokenizer, T5ForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
model = T5ForSequenceClassification.from_pretrained("google-t5/t5-small")

inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
model.config.id2label[predicted_class_id]
...

# To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
num_labels = len(model.config.id2label)
model = T5ForSequenceClassification.from_pretrained("google-t5/t5-small", num_labels=num_labels)

labels = torch.tensor([1])
loss = model(**inputs, labels=labels).loss
round(loss.item(), 2)
...
Example of multi-label classification:

Copied
import torch
from transformers import AutoTokenizer, T5ForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
model = T5ForSequenceClassification.from_pretrained("google-t5/t5-small", problem_type="multi_label_classification")

inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_ids = torch.arange(0, logits.shape[-1])[torch.sigmoid(logits).squeeze(dim=0) > 0.5]

# To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
num_labels = len(model.config.id2label)
model = T5ForSequenceClassification.from_pretrained(
    "google-t5/t5-small", num_labels=num_labels, problem_type="multi_label_classification"
)

labels = torch.sum(
    torch.nn.functional.one_hot(predicted_class_ids[None, :].clone(), num_classes=num_labels), dim=1
).to(torch.float)
loss = model(**inputs, labels=labels).loss
T5ForTokenClassification
class transformers.T5ForTokenClassification
<
source
>
( config: T5Config )

Parameters

config (T5Config) — Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
The T5 transformer with a token classification head on top (a linear layer on top of the hidden-states output) e.g. for Named-Entity-Recognition (NER) tasks.

This model inherits from PreTrainedModel. Check the superclass documentation for the generic methods the library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads etc.)

This model is also a PyTorch torch.nn.Module subclass. Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage and behavior.

forward
"""