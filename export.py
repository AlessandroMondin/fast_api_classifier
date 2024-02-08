import ssl

import torch
import torchvision.models as models
from torchvision import transforms


ssl._create_default_https_context = ssl._create_unverified_context

# Assuming the rest of your code here to load the model and preprocess the image

# Dummy input corresponds to a single image of shape [3, 224, 224]
# Adjust the shape if necessary based on your model
dummy_input = torch.randn(1, 3, 224, 224)
model = models.mobilenet_v3_large(pretrained=True)
# Specify the path for the ONNX model
onnx_model_path = "mobilenet_v3_large.onnx"

# Export the model
torch.onnx.export(
    model,  # model being run
    dummy_input,  # model input (or a tuple for multiple inputs)
    onnx_model_path,  # where to save the model
    export_params=True,  # store the trained parameter weights inside the model file
    opset_version=11,  # the ONNX version to export the model to
    do_constant_folding=True,  # whether to execute constant folding for optimization
    input_names=["input"],  # the model's input names
    output_names=["output"],  # the model's output names
    dynamic_axes={
        "input": {0: "batch_size"},  # variable-length axes
        "output": {0: "batch_size"},
    },
)
