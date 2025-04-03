import torch
from models.LMQFormer import LMQFORMER  # Assuming this is how you import your model

# Load your custom model architecture (LMQFormer)
model = LMQFORMER()  # Initialize your model

# Step 1: Load pretrained weights
checkpoint = torch.load('./checkpoints/Snow100k.pth', map_location=torch.device('cpu'))  # Load pretrained weights to CPU
model.load_state_dict(checkpoint["state_dict"])  # Load weights into the model
model.eval()  # Set the model to evaluation mode

# Step 2: Prepare the input shape for export
input_shape = (1, 3, 1024, 1024)  # Adjusted input shape (1 batch size, 3 channels, 256x256)
example_input = torch.rand(input_shape).to('cpu')  # Create a dummy input tensor for tracing

# Step 3: Export the model to ONNX
onnx_file_path = '1024_LMQFormer_snow100k.onnx'  # Specify the output ONNX file path

torch.onnx.export(
    model,                         # The model to export
    example_input,                 # Example input tensor to trace
    onnx_file_path,                # Output ONNX file path
    export_params=True,            # Export the model's parameters
    opset_version=11,              # Set the ONNX opset version (version 11 is widely compatible)
    do_constant_folding=True,      # Enable constant folding for optimization
    input_names=['image'],        # Name of the input (change if needed)
    output_names=['output'],      # Name of the output (change if needed)
    dynamic_axes={'image': {0: 'batch_size'}, 'output': {0: 'batch_size'}},  # Allow dynamic batch size
)

print(f"Model has been successfully converted to ONNX format and saved as {onnx_file_path}")
