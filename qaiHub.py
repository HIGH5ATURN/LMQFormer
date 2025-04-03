import onnx
import qai_hub as hub
import numpy as np
from PIL import Image

# Load the ONNX model
onnx_model_path = '128_LMQFormer_snow100k.onnx'
onnx_model = onnx.load(onnx_model_path)

# Step 1: Prepare the input shape
input_shape = (1, 3, 128, 128)  # (batch_size, channels, height, width)
example_input = np.random.randn(*input_shape).astype(np.float32)

# Step 2: Submit compile job to Qualcomm AI Hub
compile_job = hub.submit_compile_job(
    model=onnx_model,
    device=hub.Device("QCS8550 (Proxy)"),
    input_specs=dict(image=input_shape),
    options="--target_runtime onnx",
)
assert isinstance(compile_job, hub.CompileJob)

# Step 3: Profile on cloud-hosted device
target_model = compile_job.get_target_model()
assert isinstance(target_model, hub.Model)

# Step 4: Submit profiling job to Qualcomm AI Hub
profile_job = hub.submit_profile_job(
    model=target_model,
    device=hub.Device("QCS8550 (Proxy)"),
)
assert isinstance(profile_job, hub.ProfileJob)

# Step 5: Load and preprocess your local image
image_path = "snow_animal_01097.jpg"  # Your uploaded image
image = Image.open(image_path).resize((128, 128))  # Resize to match model input size
input_array = np.expand_dims(
    np.transpose(np.array(image, dtype=np.float32) / 255.0, (2, 0, 1)), axis=0
)

# Run inference using the on-device model
inference_job = hub.submit_inference_job(
    model=target_model,
    device=hub.Device("QCS8550 (Proxy)"),
    inputs=dict(image=[input_array]),
)
assert isinstance(inference_job, hub.InferenceJob)

# Download the output of the inference
on_device_output = inference_job.download_output_data()
assert isinstance(on_device_output, dict)

# Step 6: Post-process the output
output_name = list(on_device_output.keys())[0]
output_image = on_device_output[output_name][0]
output_image = np.squeeze(output_image)

# Check shape and dtype
print(f"Output shape: {output_image.shape}, dtype: {output_image.dtype}")

# Convert and scale output image
if output_image.ndim == 2:
    output_image = (output_image * 255).astype(np.uint8)
elif output_image.ndim == 3:
    output_image = (output_image.transpose(1, 2, 0) * 255).astype(np.uint8)

# Convert to image and display
processed_image = Image.fromarray(output_image)
processed_image.show()

# Step 7: Download optimized model
target_model.download("128_Optimized_LMQFormer_snow100k_model.onnx")