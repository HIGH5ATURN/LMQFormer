import onnx

# Load and check the ONNX model
onnx_model = onnx.load('LMQFormer_snow100k.onnx')
onnx.checker.check_model(onnx_model)

print("ONNX model is valid!")
