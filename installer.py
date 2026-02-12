from importlib.metadata import version, PackageNotFoundError
import subprocess

requirements = {
    "torch": "2.9.0",
    "torchvision": "0.24.0",
    "onnx": "1.14.0",
    "onnxruntime": "1.21.0",
    "pycocotools": "2.0.7",
    "PyYAML": "6.0.1",
    "scipy": "1.13.0",
    "onnxslim": "0.1.31",
    "onnxruntime-gpu": "1.18.0",
    "gradio": "4.31.5",
    "opencv-python": "4.9.0.80",
    "psutil": "5.9.8",
    "py-cpuinfo": "9.0.0",
    "huggingface-hub": "0.23.2",
    "safetensors": "0.4.3",
}

def is_raspberry_pi():
    try:
        with open("/proc/device-tree/model") as f:
            return "Raspberry Pi" in f.read()
    except:
        return False

def run(cmd):
    print(f"> {cmd}")
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print("Going to next step...\n")

pi = is_raspberry_pi()

# Runtime
print(f"NOTE: Not every dependency is needed to run/train the model\n")

for pkg, req_version in requirements.items():
    try:
        installed = version(pkg)
        status = "OK" if installed >= req_version else f"VERSION MISMATCH (found {installed} but wanted {req_version})"
    except PackageNotFoundError:
        status = "NOT INSTALLED"

    print(f"{pkg:20} {status}")

print("\nInstalling dependencies (if any)\n")

if pi:
    print("Raspberry Pi detected...\n")
    run("pip install onnxruntime opencv-python numpy huggingface-hub")
else:
    print("Not Raspberry PI\n")
    run("pip install -r requirements.txt")
    run("pip install -e .")